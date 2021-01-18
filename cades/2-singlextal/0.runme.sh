WORKROOT=$PWD
simdir=sim

# workflow
mcvine workflow singlecrystal --outdir=$simdir --type=DGS \
    --instrument=ARCS --sample=sample

# beam
cp run-beam.sh $simdir/beam/
cd $simdir/beam
./run-beam.sh
cd $WORKROOT

# prepare for scattering
cp swdemo-scatterer.xml $simdir/sampleassembly
cp sim.yml $simdir/scattering

# test scattering
cd $simdir/scattering/
./scripts/sim.py --angle=31.0
cd $WORKROOT

# 
./create-scatter-run_sh.py $simdir/scattering
chmod +x $simdir/scattering/run.sh
sbatch job-scatter.sh
