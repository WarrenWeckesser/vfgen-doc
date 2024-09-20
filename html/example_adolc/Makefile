# Define the environmenet variable ADOLC_BASE to be the installation
# directory of ADOL-C before running this Makefile.

# Files generated for the web page:
WEBFILES = pendulum_adolc.cpp pendulum_adolc.h plotly_data.js

ALL = $(WEBFILES) plotly_data.js

all: $(ALL)

plotly_data.js: pend7.csv
	python3 ../tools/csv_to_plotly.py pend7.csv > plotly_data.js

pend7.csv: pend_solver
	bash run_solver.sh $(ADOLC_BASE)/lib

pend_solver: Makefile-pend_solver pendulum_adolc.cpp pendulum_adolc.h
	make CPPFLAGS="-I$(ADOLC_BASE)/include -std=c++17" LDFLAGS=-L$(ADOLC_BASE)/lib -f Makefile-pend_solver

pendulum_adolc.cpp pendulum_adolc.h: ../example_vf/pendulum.vf
	vfgen adolc ../example_vf/pendulum.vf

clean:
	rm -f pend7.csv *.tap *.o pend_solver

purge: clean
	rm -f $(WEBFILES)
