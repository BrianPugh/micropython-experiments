# micropython-experiments

MicroPython Experiments is a repository containing snippets of code for
testing minimal examples of how micropython performs.

# Usage

It is recommended to use [Poetry](https://python-poetry.org) to manage
desktop python dependencies, and
[Belay](https://github.com/BrianPugh/belay) to manage micropython
dependencies and run scripts. Once Poetry and Belay are installed, the
setup process will look like:

``` bash
poetry run belay install /dev/ttyUSB0  # Use your board port.
```

Then, run a specific script on-device:

``` bash
poetry run belay run /dev/ttyUSB0 micropython-experiments/experiment1/main.py
```

# Summary of Results
