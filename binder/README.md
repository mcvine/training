[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mcvine/training/master)

https://mybinder.org/v2/gh/mcvine/training/master


To create the environment.yml, make sure channels are good, then

```
$ conda create -n mcvine python=2
$ source activate mcvine
$ conda install mcvine
$ conda update mcvine-core mcvine.instruments mcvine.phonon mcvine.workflow mantid2mcvine
$ conda install mcvine.ui
```

After installation, export
```
$ conda env export > environment.yml
```
Remove name on the top and prefix at the end.

