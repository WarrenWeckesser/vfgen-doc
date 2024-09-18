WEBFILES = pendulum_gvf.c pendulum_gvf.h pendulum_solve.c Makefile-pendulum \
           pendulum.csv

VFGEN_OUTPUT = Makefile-pendulum pendulum_gvf.c pendulum_gvf.h pendulum_solve.c
ALL = plotly_data.js pendulum.csv $(VFGEN_OUTPUT)

all: $(ALL)

plotly_data.js: pendulum.csv
	python3 ../tools/csv_to_plotly.py pendulum.csv > plotly_data.js

pendulum.csv: pendulum_solve
	./pendulum_solve v=0.0 theta=3.14 b=0.2 abserr=1e-9 stoptime=10 > pendulum.csv

pendulum_solve: $(VFGEN_OUTPUT)
	make -f Makefile-pendulum

$(VFGEN_OUTPUT): ../example_vf/pendulum.vf
	vfgen gsl:func=yes,demo=yes ../example_vf/pendulum.vf

clean:
	rm -f *.o pendulum_solve

purge:
	rm -f $(ALL) *.o pendulum_solve
