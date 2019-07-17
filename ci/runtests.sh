#!/bin/bash -ex

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

pytest -x -vv .

codecov