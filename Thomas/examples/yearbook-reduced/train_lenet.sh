#!/usr/bin/env sh
set -e

./build/tools/caffe train --solver=examples/yearbook-reduced/lenet_solver.prototxt $@
