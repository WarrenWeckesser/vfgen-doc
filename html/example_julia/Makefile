WEBFILES = lorenz.jl lorenz_demo.jl lorenz_plot.svg delayed_logistic.jl delayed_logistic_demo.jl delayed_logistic_plot.svg

VFGEN_LORENZ = lorenz.jl lorenz_demo.jl
VFGEN_DELAYED_LOGISTIC = delayed_logistic.jl delayed_logistic_demo.jl

all: $(WEBFILES)

lorenz_plot.svg: $(VFGEN_LORENZ)
	julia lorenz_demo.jl stoptime=40

$(VFGEN_LORENZ): ../example_vf/lorenz.vf
	vfgen julia:demo=yes ../example_vf/lorenz.vf

delayed_logistic_plot.svg: $(VFGEN_DELAYED_LOGISTIC)
	julia delayed_logistic_demo.jl stoptime=25

$(VFGEN_DELAYED_LOGISTIC): ../example_vf/delayed_logistic.vf
	vfgen julia:demo=yes ../example_vf/delayed_logistic.vf

clean:

purge:
	rm -f $(WEBFILES)
