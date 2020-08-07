#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=7GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=davidvng@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=dmeff_n0_loguniform.log

srun python3 dmeff_n0_loguniform.py
