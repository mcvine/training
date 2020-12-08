#!/usr/bin/env python
# coding: utf-8

# # Purpose
# * Instrument: HYSPEC
#  - Ei=7meV 
# * Sample: K2V3O8
#  - A fake sample to show a spin wave

# # Running environments

import os, shutil
thisdir = os.path.abspath(os.path.dirname(__file__))

# modify this!!!
# working directory. all inputs and outputs will be in this directory
workdir = os.path.expanduser('~/simulations/HYSPEC/spinwave-tut-use_script')
if os.path.exists(workdir):
    shutil.rmtree(workdir)
os.makedirs(workdir)
os.chdir(workdir)

# # Tools
from matplotlib import pyplot as plt
import numpy as np
import histogram.hdf as hh, histogram as H
import mcvine

# # Create workflow
# ## Sample spec
# This is a fake spin-wave model.
shutil.copyfile(os.path.join(thisdir, 'spinwave-tut/kvo.yml'), 'kvo.yml')

def exec_cmd(cmd):
    if os.system(cmd): raise RuntimeError("{} failed".format(cmd))
# ## Create workflow
cmd = 'mcvine workflow singlecrystal --instrument=hyspec --sample=kvo.yml --outdir=sim --type=DGS'
exec_cmd(cmd)

# # Beam simulation
os.chdir(os.path.join(workdir, 'sim/beam'))
os.system('rm *')
shutil.copyfile(os.path.join(thisdir, 'spinwave-tut/run-beam.sh'), 'run-beam-tmp.sh')

# ## Run beam sim
# * This will take a while to run
exec_cmd('bash ./run-beam-tmp.sh >log.run-tmp')

# sim scattering
os.chdir(os.path.join(workdir, 'sim/scattering'))


# ## Customize sim configuration
shutil.copyfile(os.path.join(thisdir, 'spinwave-tut/sim.yml'), 'sim.yml')

# ## Modify Makefile: HYSPEC need det vessel angle
shutil.copyfile(os.path.join(thisdir, 'spinwave-tut/Makefile'), 'template/Makefile')

# ## Update sample
# new sample spec
shutil.copyfile(os.path.join(thisdir, 'spinwave-tut/kvo-scatterer.xml'), '../sampleassembly/kvo-scatterer.xml')

# ## Run all angles
shutil.copyfile(os.path.join(thisdir, 'spinwave-tut/run.sh'), 'run.sh')

# run simulation (next cell). this will take a while
# run in a terminal
#  $ tail -f {workdir}/sim/scattering/log.run 
# to monitor the progress
exec_cmd('bash ./run.sh >log.run')

# # Reduction
# !mcvine workflow sxr reduce --help
# ## DGS reduction
cmd =r"""mcvine workflow sxr reduce --type batch \
       --eaxis -3 6.5 0.1 --psi-axis -50 40.1 .5 --eiguess 7 \
       --eventnxs work_%s/sim.nxs --out reduced_%s.nxs \
       > log.reduce"""
exec_cmd(cmd)

# ## Get a slice
shutil.copyfile(os.path.join(thisdir, 'spinwave-tut/slice_H10.yml'), 'slice_H10.yml')
cmd = 'time mcvine workflow sxr slice     --sample {workdir}/kvo.yml     --psi-axis -50 40.1 3.     --nxs reduced_%s.nxs     --slice slice_H10.yml     --out slice_H10.nxs     > log.slice_H10'.format(workdir=workdir)
exec_cmd(cmd)

# convert slice nexus to slice histogram
exec_cmd('mcvine workflow sxr slice2hist slice_H10.nxs slice_H10.h5')
