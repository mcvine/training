#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=30
#SBATCH --nodes=1
#SBATCH --tasks-per-node=20
#SBATCH --constraint=haswell
#SBATCH --mail-user=linjiao@ornl.gov
#SBATCH --mail-type=BEGIN,END,FAIL

export MCVINE_MPI_LAUNCHER=slurm
export HDF5_USE_FILE_LOCKING=FALSE

export PATH=$HOME/.conda/envs/mcvine-py38/bin:$PATH

which python
which mcvine

# mcvine
mcvine instruments sequoia beam --E=30.0 --fermi_nu=120.0 --fermi_chopper=700-3.56-AST --ncount=1e6 --nodes=10 --T0_nu=60.0
