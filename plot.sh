#!/usr/bin/bash

# Plots a timeseries using temp.tsv file 
# produced by plot.py as an input

python plot.py
gnuplot plot.gp 
rm temp.tsv

