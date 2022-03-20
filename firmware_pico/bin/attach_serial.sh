#!/bin/bash

#Leave minicom: CTRL+A, then press X
minicom -b 115200 -o -D "$1"