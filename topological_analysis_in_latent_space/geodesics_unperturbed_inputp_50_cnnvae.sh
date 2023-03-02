#!/bin/bash

#Submit this script with: sbatch thefilename

#SBATCH -c 8  # number of processor cores (i.e. threads)
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH --time=8:00:00   # walltime
#SBATCH -J "cnnvae"   # job name

#module purge                                 # purge if you already have modules loaded
/home/ramana44/.conda/envs/myenv/bin/python3.9 /home/ramana44/topological-analysis-of-curved-spaces-and-hybridization-of-autoencoders/topological_analysis_in_latent_space/geodesics_unperturbed_inputp_50_cnnvae.py

# Set the max number of threads to use for programs using OpenMP. Should be <= ppn. Does nothing if the program doesn't use OpenMP.
export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE
OUTFILE=""

exit 0