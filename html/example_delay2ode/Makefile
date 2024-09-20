WEBFILES = simpledelay_2ode.vf example1_plotly_data.js \
           MackeyGlass_2ode.vf example2_plotly_data.js

GSL_SIMPLE_SOURCE = Makefile-simpledelay_2ode simpledelay_2ode_gvf.c\
                    simpledelay_2ode_gvf.h simpledelay_2ode_solve.c
GSL_MG_SOURCE = Makefile-MackeyGlass_2ode MackeyGlass_2ode_gvf.c \
                MackeyGlass_2ode_gvf.h MackeyGlass_2ode_solve.c


all: example1_plotly_data.js example2_plotly_data.js

example1_plotly_data.js: outp2n12.csv
	python3 ../tools/csv_to_plotly.py outp2n12.csv "x=x(t)" "lag1_1_12=x(t-1)" > example1_plotly_data.js

outp2n12.csv: simpledelay_2ode_solve
	./simpledelay_2ode_solve relerr=1e-12 > outp2n12.csv

simpledelay_2ode_solve: $(GSL_SIMPLE_SOURCE)	
	make -f Makefile-simpledelay_2ode

$(GSL_SIMPLE_SOURCE): simpledelay_2ode.vf
	vfgen gsl:demo=yes simpledelay_2ode.vf

simpledelay_2ode.vf: ../example_vf/simpledelay.vf
	vfgen delay2ode:N=12,p=2 ../example_vf/simpledelay.vf > simpledelay_2ode.vf


example2_plotly_data.js: mg.csv
	python3 ../tools/csv_to_plotly.py mg.csv "x=x(t)" "lag1_1_25=x(t-17)" > example2_plotly_data.js

mg.csv: MackeyGlass_2ode_solve
	./MackeyGlass_2ode_solve relerr=1e-8 abserr=1e-10 stoptime=500 > mg.csv

MackeyGlass_2ode_solve: $(GSL_MG_SOURCE)
	make -f Makefile-MackeyGlass_2ode

$(GSL_MG_SOURCE): MackeyGlass_2ode.vf
	vfgen gsl:demo=yes MackeyGlass_2ode.vf

MackeyGlass_2ode.vf: ../example_vf/MackeyGlass.vf
	vfgen delay2ode:N=25,p=3 ../example_vf/MackeyGlass.vf > MackeyGlass_2ode.vf


clean:
	rm -f *.o
	rm -f $(GSL_SIMPLE_SOURCE) simpledelay_2ode_solve outp2n12.csv
	rm -f $(GSL_MG_SOURCE) MackeyGlass_2ode_solve mg.csv

purge:
	rm -f *.o
	rm -f simpledelay_2ode.vf $(GSL_SIMPLE_SOURCE) simpledelay_2ode_solve outp2n12.csv example1_plotly_data.js
	rm -f MackeyGlass_2ode.vf $(GSL_MG_SOURCE) MackeyGlass_2ode_solve mg.csv example2_plotly_data.js
