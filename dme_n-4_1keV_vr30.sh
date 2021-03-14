#!/bin/bash
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=24
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=7GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=sarnaaik@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=dme_n-4_1keV_vr30.log

srun cobaya-run dme_n-4_1keV_vr30.yaml
