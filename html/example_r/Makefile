
WEBFILES = pendulumv.R pendulumv_demo.R MackeyGlass.R MackeyGlass_demo.R \
           pendulumv_demo.svg plot_pendulumv_solution.svg MackeyGlass_demo.svg

VFGEN_EXAMPLE1_OUTPUT = pendulumv.R pendulumv_demo.R
VFGEN_EXAMPLE2_OUTPUT = MackeyGlass.R MackeyGlass_demo.R


all: example1 example2

#
# Example 1
#

example1: $(VFGEN_EXAMPLE1_OUTPUT) pendulumv_demo.svg plot_pendulumv_solution.svg

$(VFGEN_EXAMPLE1_OUTPUT): ../example_vf/pendulumv.vf
	vfgen r:func=yes,demo=yes ../example_vf/pendulumv.vf

pendulumv_demo.svg: run_pendulumv_demo.R $(VFGEN_EXAMPLE1_OUTPUT)
	R --vanilla --slave -f run_pendulumv_demo.R

plot_pendulumv_solution.svg: plot_pendulumv_solution.R $(VFGEN_EXAMPLE1_OUTPUT)
	R --vanilla --slave -f plot_pendulumv_solution.R

#
# Example 2
#

example2: $(VFGEN_EXAMPLE2_OUTPUT) MackeyGlass_demo.svg

$(VFGEN_EXAMPLE2_OUTPUT): ../example_vf/MackeyGlass.vf
	vfgen r:demo=yes ../example_vf/MackeyGlass.vf

MackeyGlass_demo.svg: MackeyGlass_demo.R
	R --vanilla --slave -f run_MackeyGlass_demo.R --args stoptime 500

#
# Clean up
#

purge:
	rm -f $(VFGEN_EXAMPLE1_OUTPUT) $(VFGEN_EXAMPLE2_OUTPUT) \
	      pendulumv_demo.svg plot_pendulumv_solution.svg MackeyGlass_demo.svg
