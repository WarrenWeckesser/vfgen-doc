WEBFILES = lorenz.jl lorenz_demo.jl lorenz_plot.svg

VFGEN_OUTPUT = lorenz.jl lorenz_demo.jl

lorenz_plot.svg: $(VFGEN_OUTPUT)
	julia lorenz_demo.jl

$(VFGEN_OUTPUT): ../example_vf/lorenz.vf
	vfgen julia:demo=yes ../example_vf/lorenz.vf

clean:

purge:
	rm -f $(VFGEN_OUTPUT) lorenz_plot.svg
