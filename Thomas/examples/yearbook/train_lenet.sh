#!/usr/bin/env sh
set -e

./build/tools/caffe train --solver=examples/yearbook/lenet_solver.prototxt $@
