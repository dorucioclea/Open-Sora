# Define dataset
dataset = dict(
    type="VariableVideoTextDataset",
    data_path=None,
    num_frames=None,
    frame_interval=3,
    image_size=(None, None),
    transform_name="resize_crop",
)
# IMG: 1024 (20%) 512 (30%) 256 (50%) drop (50%)
bucket_config = {  # 1s/it
    "144p": {16: (1.0, 8), 32: (1.0, 4), 64: (1.0, 2), 128: (1.0, 1)},
    "256": {1: (0.5, 32), 16: (0.5, 4), 32: (0.5, 2), 64: (0.5, 1), 128: (0.0, None)},
    "240p": {16: (0.3, 3), 32: (0.3, 1), 64: (0.0, None)},
    "512": {1: (0.4, 16)},
    "1024": {1: (0.3, 4)},
}
mask_ratios = {
    "mask_no": 0.9,
    "mask_quarter_random": 0.01,
    "mask_quarter_head": 0.01,
    "mask_quarter_tail": 0.01,
    "mask_quarter_head_tail": 0.02,
    "mask_image_random": 0.01,
    "mask_image_head": 0.01,
    "mask_image_tail": 0.01,
    "mask_image_head_tail": 0.02,
}

# Define acceleration
num_workers = 8
num_bucket_build_workers = 16
dtype = "bf16"
grad_checkpoint = False
plugin = "zero2"
sp_size = 1

# Define model
model = dict(
    type="STDiT2-XL/2",
    from_pretrained=None,
    input_sq_size=512,  # pretrained model is trained on 512x512
    enable_flashattn=True,
    enable_layernorm_kernel=True,
)
vae = dict(
    type="VideoAutoencoderKL",
    from_pretrained="stabilityai/sd-vae-ft-ema",
    micro_batch_size=4,
    local_files_only=True,
)
text_encoder = dict(
    type="t5",
    from_pretrained="DeepFloyd/t5-v1_1-xxl",
    model_max_length=200,
    shardformer=True,
    local_files_only=True,
)
scheduler = dict(
    type="iddpm-speed",
    timestep_respacing="",
)

# Others
seed = 42
outputs = "outputs"
wandb = False

epochs = 1000
log_every = 10
ckpt_every = 500
load = None

batch_size = None
lr = 2e-5
grad_clip = 1.0