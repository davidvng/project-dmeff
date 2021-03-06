#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=24
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=7GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=sarnaaik@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=lcdm_drag_test_run2.log

srun cobaya-run chains/dmeff_drag_lcdm_test
