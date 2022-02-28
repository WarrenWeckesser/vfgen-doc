WEBFILES = simpledelay_2ode.vf delay_plot_p2n12.svg \
           MackeyGlass_2ode.vf mg.svg

GSL_SIMPLE_SOURCE = Makefile-simpledelay_2ode simpledelay_2ode_gvf.c\
                    simpledelay_2ode_gvf.h simpledelay_2ode_solve.c
GSL_MG_SOURCE = Makefile-MackeyGlass_2ode MackeyGlass_2ode_gvf.c \
                MackeyGlass_2ode_gvf.h MackeyGlass_2ode_solve.c


all: delay_plot_p2n12.svg mg.svg


delay_plot_p2n12.svg: outp2n12.dat delay_plot.py
	python delay_plot.py

outp2n12.dat: simpledelay_2ode_solve
	./simpledelay_2ode_solve relerr=1e-12 > outp2n12.dat

simpledelay_2ode_solve: $(GSL_SIMPLE_SOURCE)	
	make -f Makefile-simpledelay_2ode

$(GSL_SIMPLE_SOURCE): simpledelay_2ode.vf
	vfgen gsl:demo=yes simpledelay_2ode.vf

simpledelay_2ode.vf: ../example_vf/simpledelay.vf
	vfgen delay2ode:N=12,p=2 ../example_vf/simpledelay.vf > simpledelay_2ode.vf


mg.svg: mg.dat mg_plot.py
	python mg_plot.py

mg.dat: MackeyGlass_2ode_solve
	./MackeyGlass_2ode_solve relerr=1e-8 abserr=1e-10 stoptime=500 > mg.dat

MackeyGlass_2ode_solve: $(GSL_MG_SOURCE)
	make -f Makefile-MackeyGlass_2ode

$(GSL_MG_SOURCE): MackeyGlass_2ode.vf
	vfgen gsl:demo=yes MackeyGlass_2ode.vf

MackeyGlass_2ode.vf: ../example_vf/MackeyGlass.vf
	vfgen delay2ode:N=25,p=3 ../example_vf/MackeyGlass.vf > MackeyGlass_2ode.vf


clean:
	rm -f *.o
	rm -f $(GSL_SIMPLE_SOURCE) simpledelay_2ode_solve outp2n12.dat
	rm -f $(GSL_MG_SOURCE) MackeyGlass_2ode_solve mg.dat

purge:
	rm -f *.o
	rm -f simpledelay_2ode.vf $(GSL_SIMPLE_SOURCE) simpledelay_2ode_solve outp2n12.dat delay_plot_p2n12.svg
	rm -f MackeyGlass_2ode.vf $(GSL_MG_SOURCE) MackeyGlass_2ode_solve mg.dat mg.svg
