WEBFILES = pendulum_cv7.c pendulum_cv7.h pendulum_cv7demo.c Makefile-pendulum_cv7demo \
           CMakeLists.txt pend.dat pendplot.png

VFGEN_OUTPUT = Makefile-pendulum_cv7demo CMakeLists.txt pendulum_cv7.c pendulum_cv7.h pendulum_cv7demo.c
ALL = pendplot.png pend.dat $(VFGEN_OUTPUT)

all: $(ALL)

pendplot.png: pendulum_plot.py pend.dat
	python3 pendulum_plot.py

pend.dat: pendulum_cv7demo
	./pendulum_cv7demo v=0.0 theta=3.14 b=0.5 stoptime=10 > pend.dat

pendulum_cv7demo: $(VFGEN_OUTPUT)
	make -f Makefile-pendulum_cv7demo

$(VFGEN_OUTPUT): ../example_vf/pendulum.vf
	vfgen cvode7:func=yes,demo=yes ../example_vf/pendulum.vf

clean:
	rm -f *.o pendulum_cv7demo

purge:
	rm -f $(ALL) *.o pendulum_cv7demo
