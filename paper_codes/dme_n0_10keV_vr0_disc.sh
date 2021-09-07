#!/bin/bash
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=16
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=davidvng@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=dme_n0_10keV_vr0_disc.log

srun cobaya-run dme_n0_10keV_vr0.yaml
