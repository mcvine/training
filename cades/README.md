# Run mcvine at ORNL CADES
## Connect to `or-slurm-login.ornl.gov`
## Install mcvine

### Install mcvine using conda
```
$ module purge
$ module load anaconda3/5.1.0
$ conda config --add channels conda-forge
$ conda config --add channels diffpy
$ conda config --add channels mantid
$ conda config --add channels mcvine
$ conda create -n mcvine3 -c mcvine/label/unstable mcvine=1.4.0 mcvine-core=1.4.1.dev python=3 openmpi
$ source activate mcvine3
```

## Create ~/.mantid if necessary

```$ git clone https://github.com/yxqd/dotmantid.git ~/.mantid```

## Run examples
See sub-folders here
