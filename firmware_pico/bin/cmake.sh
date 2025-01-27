#!/bin/bash

#Used for generating machine specific build configuration (Makefile) in build directory

basedir="$(dirname $0)/.."

rm -rf "${basedir}/build"
if [ "$1" = "debug" ]; then
  echo "generating debug version"
  cmake -S "${basedir}" -B "${basedir}/build" -DCMAKE_BUILD_TYPE=Debug
else
  cmake -S "${basedir}" -B "${basedir}/build"
fi
