WEBFILES = vanderpol_rhs.f vanderpol_dr5.f

VFGEN_OUTPUT = vanderpol_rhs.f vanderpol_dr5.f
OBJS = vanderpol_dr5.o vanderpol_rhs.o radau5.o dc_lapack.o
ALL = $(VFGEN_OUTPUT) plotly_data.js vdp.csv vanderpol_dr5

all: $(ALL)

plotly_data.js: vdp.csv
	python3 ../tools/csv_to_plotly.py vdp.csv > plotly_data.js

vdp.csv: vanderpol_dr5
	./vanderpol_dr5 > vdp.csv

vanderpol_dr5:	$(OBJS)
	gfortran $(OBJS) -llapack -o vanderpol_dr5

%.o: %.f
	gfortran -c $<

$(VFGEN_OUTPUT): ../example_vf/vanderpol.vf
	vfgen radau5:demo=yes ../example_vf/vanderpol.vf


clean:
	rm -f *.o vdp.csv vanderpol_dr5

purge:
	rm -f $(ALL) *.o
