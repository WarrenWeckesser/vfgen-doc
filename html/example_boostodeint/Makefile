WEBFILES = pendulum_vf.cpp pendulum_vf.h pendulum_demo.cpp Makefile.pendulum_demo

VFGEN_OUTPUT = pendulum_vf.cpp pendulum_vf.h pendulum_demo.cpp Makefile.pendulum_demo
OBJS = pendulum_demo.o pendulum_vf.o
ALL = $(VFGEN_OUTPUT) plotly_data.js pendulum_data.csv pendulum_demo

all: plotly_data.js

plotly_data.js: pendulum_data.csv
	python ../tools/csv_to_plotly.py pendulum_data.csv > plotly_data.js

pendulum_data.csv: pendulum_demo
	./pendulum_demo > pendulum_data.csv

pendulum_demo: $(VFGEN_OUTPUT)
	make -f Makefile.pendulum_demo

$(VFGEN_OUTPUT): ../example_vf/pendulum.vf
	vfgen boostodeint:system=implicit,demo=yes ../example_vf/pendulum.vf

purge:
	rm -f $(ALL) *.o
