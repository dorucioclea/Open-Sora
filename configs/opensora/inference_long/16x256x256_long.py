num_frames = 16
fps = 24 // 3
image_size = (256, 256)

# Define model
model = dict(
    type="STDiT-XL/2",
    space_scale=0.5,
    time_scale=1.0,
    enable_flashattn=True,
    enable_layernorm_kernel=True,
    from_pretrained="PRETRAINED_MODEL",
)
vae = dict(
    type="VideoAutoencoderKL",
    from_pretrained="stabilityai/sd-vae-ft-ema",
    micro_batch_size=4,
)
text_encoder = dict(
    type="t5",
    from_pretrained="./pretrained_models/t5_ckpts",
    model_max_length=120,
)
scheduler = dict(
    type="iddpm",
    num_sampling_steps=100,
    cfg_scale=7.0,
)
dtype = "fp16"

# Condition
prompt_path = None
prompt = [
    "In an ornate, historical hall, a massive tidal wave peaks and begins to crash. Two surfers, seizing the moment, skillfully navigate the face of the wave."
]

loop = 10
condition_frame_length = 4
reference_path = ["assets/images/condition/wave.png"]
mask_strategy = ["0,0,0,1,0"]  # valid when reference_path is not None
# loop id, ref id, ref start, length, target start

# Others
batch_size = 2
seed = 42
save_dir = "./samples/"