WEBFILES = pendulum.py pendulum_demo.py pendulum_plot.svg

VFGEN_OUTPUT = pendulum.py pendulum_demo.py
ALL = pend.dat pendulum_plot.svg $(VFGEN_OUTPUT)

all: $(ALL)

pendulum_plot.svg: pend.dat pendulum_plot.py
	python pendulum_plot.py

pend.dat: pendulum_demo.py pendulum.py
	python pendulum_demo.py theta=3.1 b=0.5 stoptime=10 > pend.dat

$(VFGEN_OUTPUT): ../example_vf/pendulum.vf
	vfgen scipy:func=yes,demo=yes ../example_vf/pendulum.vf

clean:
	rm -rf pend.dat __pycache__

purge:
	rm -rf $(ALL) __pycache__
