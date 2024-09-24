FC = gfortran

WEBFILES = MackeyGlass.f90 MackeyGlass_demo.f90 plotly_example1_data.js \
           sdd.f90 sdd_demo.f90 sdd.svg \
           sddfn.f90 sddfn_demo.f90 sddfn.svg

MG_VFGEN_FILES = MackeyGlass.f90 MackeyGlass_demo.f90
SDD_VFGEN_FILES = sdd.f90 sdd_demo.f90
SDDFN_VFGEN_FILES = sddfn.f90 sddfn_demo.f90

all: example1 example2 example3

#
# Example 1
#

example1: plotly_example1_data.js

plotly_example1_data.js: mg.csv
	python ../tools/csv_to_plotly.py mg.csv > plotly_example1_data.js

mg.csv: MackeyGlass_demo
	./MackeyGlass_demo > mg.csv

MackeyGlass_demo_stoptime500.f90: MackeyGlass_demo.f90
	sed 's/stoptime = 10\.0/stoptime = 500.0/' MackeyGlass_demo.f90 > MackeyGlass_demo_stoptime500.f90

MackeyGlass_demo: MackeyGlass_demo_stoptime500.f90 MackeyGlass.f90 dde_solver_m.o
	$(FC) MackeyGlass.f90 MackeyGlass_demo_stoptime500.f90  dde_solver_m.o -o MackeyGlass_demo

$(MG_VFGEN_FILES): ../example_vf/MackeyGlass.vf
	vfgen dde_solver:demo=yes ../example_vf/MackeyGlass.vf

#
# Example 2
#

example2: sdd.svg

sdd.svg:  sdd.csv sdd_plot.py
	python sdd_plot.py

sdd.csv: sdd_demo
	./sdd_demo > sdd.csv

sdd_demo: $(SDD_VFGEN_FILES) dde_solver_m.o
	$(FC) $(SDD_VFGEN_FILES)  dde_solver_m.o -o sdd_demo

$(SDD_VFGEN_FILES): ../example_vf/sdd.vf
	vfgen dde_solver:demo=yes ../example_vf/sdd.vf

#
# Example 3
#

example3: sddfn.svg

sddfn.svg: sddfn.csv sddfn_plot.py
	python sddfn_plot.py

sddfn.csv: sddfn_demo
	./sddfn_demo > sddfn.csv

sddfn_demo: sddfn_demo_stoptime2.f90 sddfn.f90 dde_solver_m.o
	$(FC) sddfn.f90 sddfn_demo_stoptime2.f90 dde_solver_m.o -o sddfn_demo

sddfn_demo_stoptime2.f90: sddfn_demo.f90
	sed -e 's/stoptime = 10\.0/stoptime = 2.0/' \
        -e 's/relerr = 1D-7/relerr = 1D-9/' \
        -e 's/abserr = 1D-9/abserr = 1D-11/' \
        sddfn_demo.f90 > sddfn_demo_stoptime2.f90

$(SDDFN_VFGEN_FILES): ../example_vf/sddfn.vf
	vfgen dde_solver:demo=yes ../example_vf/sddfn.vf


dde_solver_m.o: dde_solver_m.f90
	$(FC) -c dde_solver_m.f90


clean:
	rm -f *.o *.mod
	rm -f mg.dat MackeyGlass_demo_stoptime500.f90 MackeyGlass_demo
	rm -f sdd.dat sdd_demo
	rm -f sddfn.dat sddfn_demo_stoptime2.f90 sddfn_demo

purge:
	rm -f *.o *.mod
	rm -f plotly_example1_data.js mg.csv MackeyGlass_demo_stoptime500.f90 \
          $(MG_VFGEN_FILES) MackeyGlass_demo
	rm -f sdd.svg sdd.csv $(SDD_VFGEN_FILES) sdd_demo
	rm -f sddfn.svg sddfn.csv sddfn_demo_stoptime2.f90 \
          $(SDDFN_VFGEN_FILES) sddfn_demo
