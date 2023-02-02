#!/bin/bash

#Submit this script with: sbatch thefilename

#SBATCH -c 8  # number of processor cores (i.e. threads)
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH --time=2:00:00   # walltime
#SBATCH -J "noiseco"   # job name

#module purge                                 # purge if you already have modules loaded
/home/ramana44/.conda/envs/myenv/bin/python3.9 /home/ramana44/topological-analysis-of-curved-spaces-and-hybridization-of-autoencoders/topological_analysis_in_latent_space/just_get_me_perturbed_images_and_coefficients_of_perturbed_images.py

# Set the max number of threads to use for programs using OpenMP. Should be <= ppn. Does nothing if the program doesn't use OpenMP.
export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE
OUTFILE=""

exit 0