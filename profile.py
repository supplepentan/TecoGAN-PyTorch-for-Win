import argparse
import os

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("degradation")
parser.add_argument("model")
parser.add_argument("lr_size")
args = parser.parse_args()

# basic settings
root_dir = "."
gpu_ids = "0"

# run
os.system(
    f"python {root_dir}/codes/main.py --exp_dir {root_dir}/experiments_{args.degradation}/{args.model} --mode profile --opt test.yml --gpu_ids {gpu_ids} --lr_size {args.lr_size} --test_speed"
)
