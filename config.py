class Config:
    model_family: str = "openvla"

    # 模型路径
    pretrained_checkpoint: str = "/mnt/workspace/openvla-7b-finetuned-libero-spatial"
    # pretrained_checkpoint: str = "/mnt/workspace/openvla-7b"

    # lora 权重路径
    lora_checkpoint: str | None = None

    # 使用量化
    load_in_8bit: bool = True
    load_in_4bit: bool = False

    # LIBERO 场景，可选: libero_spatial, libero_object, libero_goal, libero_10, libero_90
    task_suite_name: str = "libero_spatial"
    
    # 每个任务重复执行的次数
    num_trials_per_task: int = 2

    # 每个任务的最大时间步（超过则截断）
    max_steps: int = 220

    # 是否在推理时为每一帧生成基于当前视觉的逐步 CoT
    enable_frame_cot: bool = True

    # 逐帧 CoT 的生成长度
    cot_max_new_tokens: int = 128

    local_log_dir: str = "./experiments/logs"        # Local directory for eval logs


""" libero 中各个任务的最长步数
if cfg.task_suite_name == "libero_spatial":
    max_steps = 220  # longest training demo has 193 steps
elif cfg.task_suite_name == "libero_object":
    max_steps = 280  # longest training demo has 254 steps
elif cfg.task_suite_name == "libero_goal":
    max_steps = 300  # longest training demo has 270 steps
elif cfg.task_suite_name == "libero_10":
    max_steps = 520  # longest training demo has 505 steps
elif cfg.task_suite_name == "libero_90":
    max_steps = 400  # longest training demo has 373 steps
"""