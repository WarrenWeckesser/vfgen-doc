
reset
set encoding utf8
set colorsequence podo
set terminal pngcairo size 360,240 enhanced font "Verdana,10"
set output "pendulum.png"
set title "Pendulum"
set xlabel "t"
set grid
plot "pendulum.out" using 1:2 title "θ" with lines linestyle 1, \
     "pendulum.out" using 1:3 title "v" with lines linestyle 2 dashtype (12,6)
