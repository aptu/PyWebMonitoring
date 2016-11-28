#!/usr/bin/gnuplot

set terminal png enhanced size 2800, 400
set output "plot.png"
set title "Traffic time series"

set ylabel "RPS (1-minute range)"
set xlabel "Time"

set xdata time
set timefmt "%s"
set xtics 60

set grid
set key left box

plot "temp.tsv" using 1:2 smooth csplines title "200", \
     "temp.tsv" using 1:3 smooth csplines title "404", \
     "temp.tsv" using 1:4 smooth csplines title "500"
