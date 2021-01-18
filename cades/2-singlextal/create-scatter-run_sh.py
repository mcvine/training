#!/usr/bin/env python
import sys
wd = sys.argv[1]
import numpy as np
ostream = open('{}/run.sh'.format(wd), 'wt')
for a in np.arange(-90, 90.1, 3.):
    ostream.write('./scripts/sim.py --angle=%s \n' % a)
    continue
ostream.close()
