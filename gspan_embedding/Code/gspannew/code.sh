#!/bin/sh 
 
#SBATCH -o gpu-job-%j.output
#SBATCH -p NV100q 
#SBATCH --gres=gpu:1 
#SBATCH -n 1

python main1.py > out.txt
