#!/bin/bash

#SBATCH -N 1
#SBATCH -n 10
#SBATCH -c 1
#SBATCH -A birthright
#SBATCH -J seq-powder-scatter
#SBATCH -p burst
#SBATCH --mail-user=linjiao@ornl.gov
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mem=0
#SBATCH -t 00:59:00
#SBATCH -o ./output.txt
#SBATCH -e ./error.txt
module purge
module load anaconda3/5.1.0
# module load mpich/3.2
# module load PE-gnu

#source activate mcvine
export PATH=$HOME/.conda/envs/mcvine3/bin:$PATH
which python
which mcvine

# mcvine
cd mysim
make NODES=10 NCOUNT=1e8 BUFFER_SIZE=1000000
