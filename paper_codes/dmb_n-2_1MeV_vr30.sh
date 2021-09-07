#!/bin/bash
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=16
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=sarnaaik@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=dmb_n-2_1MeV_vr30.log

srun cobaya-run dmb_n-2_1MeV_vr30.yaml
