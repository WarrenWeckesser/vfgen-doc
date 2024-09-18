WEBFILES = pendulum_cv7.c pendulum_cv7.h pendulum_cv7demo.c Makefile-pendulum_cv7demo \
           CMakeLists.txt pend.csv

VFGEN_OUTPUT = Makefile-pendulum_cv7demo CMakeLists.txt pendulum_cv7.c pendulum_cv7.h pendulum_cv7demo.c
ALL = plotly_data.js pend.csv $(VFGEN_OUTPUT)

all: $(ALL)

plotly_data.js: pendulum_plot.py pend.csv
	python3 ../tools/csv_to_plotly.py pend.csv > plotly_data.js

pend.csv: pendulum_cv7demo
	./pendulum_cv7demo v=0.0 theta=3.14 b=0.5 stoptime=10 > pend.csv

pendulum_cv7demo: $(VFGEN_OUTPUT)
	make -f Makefile-pendulum_cv7demo

$(VFGEN_OUTPUT): ../example_vf/pendulum.vf
	vfgen cvode7:func=yes,demo=yes ../example_vf/pendulum.vf

clean:
	rm -f *.o pendulum_cv7demo

purge:
	rm -f $(ALL) *.o pendulum_cv7demo
