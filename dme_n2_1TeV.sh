#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=24
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=7GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=davidvng@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=dme_n2_1TeV.log

srun cobaya-run dme_n2_1TeV.yaml
