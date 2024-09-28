# This Makefile doesn't regenerate the data files vdpgsl.dat and vdpr5.dat.
# These were created using GSL and RADAU5.

WEBFILES = pendulum_taylor7.c pendulum_taylor7.h pend7.svg pend_taylor_demo.svg \
           vdp8compare.svg


all: example1 example2

example1: pend7.svg pend_taylor_demo.svg

pend7.svg: pend7plot.py pend7.csv
	python pend7plot.py

pend7.csv: pend_main
	./pend_main > pend7.csv

pend_main: Makefile_pend_main pend_main.c pendulum_taylor7.c pendulum_taylor7.h
	make -f Makefile_pend_main

pendulum_taylor7.c pendulum_taylor7.h: ../example_vf/pendulum.vf
	vfgen taylor:order=7 ../example_vf/pendulum.vf


pend_taylor_demo.svg: pend_taylor_demo_plot.py demo_gsl.csv demo3.dat demo7.dat demo15.dat
	python pend_taylor_demo_plot.py

demo_gsl.csv: pendulum_solve
	./pendulum_solve b=0.25 L=1 m=1 theta=1 v=1.5 abserr=1e-12 relerr=1e-10 > demo_gsl.csv

pendulum_solve: ../example_vf/pendulum.vf
	vfgen gsl:demo=yes ../example_vf/pendulum.vf
	make -f Makefile-pendulum

demo3.dat: pend_taylor3_demo
	./pend_taylor3_demo > demo3.dat

pend_taylor3_demo: pend_taylor3_demo.c pendulum_taylor3.c pendulum_taylor3.h
	gcc pend_taylor3_demo.c pendulum_taylor3.c -lm -o pend_taylor3_demo

pendulum_taylor3.c pendulum_taylor3.h: ../example_vf/pendulum.vf
	vfgen taylor:order=3 ../example_vf/pendulum.vf


demo7.dat: pend_taylor7_demo
	./pend_taylor7_demo > demo7.dat

pend_taylor7_demo: pend_taylor7_demo.c pendulum_taylor7.c pendulum_taylor7.h
	gcc pend_taylor7_demo.c pendulum_taylor7.c -lm -o pend_taylor7_demo


demo15.dat: pend_taylor15_demo
	./pend_taylor15_demo > demo15.dat

pend_taylor15_demo: pend_taylor15_demo.c pendulum_taylor15.c pendulum_taylor15.h
	gcc pend_taylor15_demo.c pendulum_taylor15.c -lm -o pend_taylor15_demo

pendulum_taylor15.c pendulum_taylor15.h: ../example_vf/pendulum.vf
	vfgen taylor:order=15 ../example_vf/pendulum.vf


example2: vdp8compare.svg

vdp8.dat: ../example_vf/vanderpol.vf Makefile-vanderpol_adaptive8
	vfgen taylor:order=8 ../example_vf/vanderpol.vf
	make -f Makefile-vanderpol_adaptive8
	./vanderpol_adaptive8 > vdp8.dat

vdp8compare.svg: vdp8.dat vdpgsl.dat vdp8plot.py
	python vdp8plot.py

clean:
	rm -f *.o
	rm -f pend7.csv pend_main
	rm -f demo3.dat pend_taylor3_demo pendulum_taylor3.c pendulum_taylor3.h
	rm -f demo7.dat pend_taylor7_demo
	rm -f demo_gsl.csv
	rm -f demo15.dat pend_taylor15_demo pendulum_taylor15.c pendulum_taylor15.h
	rm -f Makefile-pendulum pendulum_solve pendulum_solve.c pendulum_gvf.c pendulum_gvf.h
	rm -f vdp8.dat vanderpol_adaptive8 vanderpol_taylor8.c vanderpol_taylor8.h

purge:
	rm -f *.o
	rm -f pend7.svg pend7.csv pend_main pendulum_taylor7.c pendulum_taylor7.h
	rm -f demo3.dat pend_taylor3_demo pendulum_taylor3.c pendulum_taylor3.h
	rm -f demo7.dat pend_taylor7_demo pendulum_taylor7.c pendulum_taylor7.h
	rm -f pend_taylor_demo.svg demo_gsl.csv
	rm -f demo15.dat pend_taylor15_demo pendulum_taylor15.c pendulum_taylor15.h
	rm -f Makefile-pendulum pendulum_solve pendulum_solve.c pendulum_gvf.c pendulum_gvf.h
	rm -f vdp8compare.svg vdp8.dat vanderpol_adaptive8 vanderpol_taylor8.c vanderpol_taylor8.h
