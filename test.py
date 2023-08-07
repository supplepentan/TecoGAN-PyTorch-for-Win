import os
import sys

# This script is used to evaluate a pretrained model.

# basic settings
root_dir = "."
degradation = sys.argv[1]
model = sys.argv[2]
gpu_ids = "2,3"
master_port = "4322"

# run
num_gpus = len(gpu_ids.split(","))
dist_args = ""
if num_gpus > 1:
    dist_args = f"-m torch.distributed.launch --nproc_per_node {num_gpus} --master_port {master_port}"

os.environ["CUDA_VISIBLE_DEVICES"] = gpu_ids
os.system(
    f"python {dist_args} {root_dir}/codes/main.py --exp_dir {root_dir}/experiments_{degradation}/{model} --mode test --opt test.yml --gpu_ids {gpu_ids}"
)
