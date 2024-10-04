# This Makefile doesn't regenerate the data files vdpgsl.dat and vdpr5.dat.
# These were created using GSL and RADAU5.

WEBFILES = pendulum_taylor7.c pendulum_taylor7.h plotly_pend7_data.js pend_taylor_demo.svg \
           vdp8compare.svg


all: example1 example2

example1: plotly_pend7_data.js pend_taylor_demo.svg

plotly_pend7_data.js: pend7.csv
	python ../tools/csv_to_plotly.py pend7.csv > plotly_pend7_data.js 

pend7.csv: pend_main
	./pend_main > pend7.csv

pend_main: Makefile_pend_main pend_main.c pendulum_taylor7.c pendulum_taylor7.h
	make -f Makefile_pend_main

pend_taylor_demo_gsl.csv: pendulum_solve
	./pendulum_solve b=0.25 L=1 m=1 theta=1 v=1.5 abserr=1e-12 relerr=1e-10 > pend_taylor_demo_gsl.csv

pendulum_solve: ../example_vf/pendulum.vf
	vfgen gsl:demo=yes ../example_vf/pendulum.vf
	make -f Makefile-pendulum

pend_taylor_demo.svg: pend_taylor_demo_plot.py pend_taylor_samples.csv pend_taylor_demo_gsl.csv
	python pend_taylor_demo_plot.py

pend_taylor_samples.csv: pend_taylor_samples_demo
	./pend_taylor_samples_demo > pend_taylor_samples.csv

pend_taylor_samples_demo: pend_taylor_samples_demo.c  pendulum_taylor15.c pendulum_taylor15.c
	$(CC) pend_taylor_samples_demo.c pendulum_taylor15.c -lm -o pend_taylor_samples_demo

pendulum_taylor7.c pendulum_taylor7.h: ../example_vf/pendulum.vf
	vfgen taylor:order=7 ../example_vf/pendulum.vf

pendulum_taylor15.c pendulum_taylor15.h: ../example_vf/pendulum.vf
	vfgen taylor:order=15 ../example_vf/pendulum.vf


example2: vdp8compare.svg

vdp8.dat: ../example_vf/vanderpol.vf Makefile-vanderpol_adaptive8
	vfgen taylor:order=8 ../example_vf/vanderpol.vf
	make -f Makefile-vanderpol_adaptive8
	./vanderpol_adaptive8 > vdp8.dat

vdp8compare.svg: vdp8.dat vdpgsl.dat vdp8plot.py
	python vdp8plot.py

# TODO: Fix the clean target.  It clean up anything that is not
# needed for the web page.
clean:
	rm -f *.o
	rm -f pend7.csv pend_main
	rm -f pend_taylor_demo_gsl.csv
	rm -f Makefile-pendulum pendulum_solve pendulum_solve.c pendulum_gvf.c pendulum_gvf.h
	rm -f vdp8.dat vanderpol_adaptive8 vanderpol_taylor8.c vanderpol_taylor8.h

purge:
	rm -f *.o
	rm -f plotly_pend7_data.js
	rm -f pend7.csv pend_main pendulum_taylor7.c pendulum_taylor7.h
	rm -f pendulum_taylor15.c pendulum_taylor15.h
	rm -f pend_taylor_samples_demo pend_taylor_samples.csv
	rm -f pend_taylor_demo.svg pend_taylor_demo_gsl.csv
	rm -f Makefile-pendulum pendulum_solve pendulum_solve.c pendulum_gvf.c pendulum_gvf.h
	rm -f vdp8compare.svg vdp8.dat vanderpol_adaptive8 vanderpol_taylor8.c vanderpol_taylor8.h
