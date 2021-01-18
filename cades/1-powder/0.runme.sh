#!/bin/bash
# Example commands
WORKROOT=$PWD

# workflow
mcvine workflow powder --instrument=sequoia --sample=V --workdir=mysim 

# beam
cp run-beam.sh mysim/beam/
cd mysim/beam
./run-beam.sh
cd $WORKROOT

# scatter/detector/reduce
sbatch job-scatter.sh
