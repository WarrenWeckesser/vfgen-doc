
reset
set encoding utf8
set colorsequence podo
set term svg
set output "pendulum.svg"
set title "Pendulum"
set xlabel "t"
set grid
plot "pendulum.out" using 1:2 title "θ" with lines linestyle 1, \
     "pendulum.out" using 1:3 title "v" with lines linestyle 2 dashtype (12,6)
