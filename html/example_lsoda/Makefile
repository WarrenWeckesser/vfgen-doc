WEBFILES = vanderpol_rhs.f vanderpol_demo.f vdp.csv rossler_rhs.f

VFGEN_EXAMPLE1_OUTPUT = vanderpol_rhs.f vanderpol_demo.f
VFGEN_EXAMPLE2_OUTPUT = rossler_rhs.f
ALL = $(VFGEN_EXAMPLE1_OUTPUT) $(VFGEN_EXAMPLE2_OUTPUT) vdp.csv plotly_vdp_data.js rp.csv rp_x_return_map.csv plotly_rp_x_return_map_data.js

LSODA_OBJS = opkdmain.o opkda1.o opkda2.o 
EXAMPLE1_OBJS = vanderpol_rhs.o vanderpol_demo.o
EXAMPLE2_OBJS = rossler_pmap.o rossler_rhs.o 

all: $(ALL)

plotly_vdp_data.js: vdp.csv
	python ../tools/csv_to_plotly.py vdp.csv > plotly_vdp_data.js

vdp.csv: vanderpol_demo
	./vanderpol_demo > vdp.csv

vanderpol_demo:	$(EXAMPLE1_OBJS) $(LSODA_OBJS)
	gfortran $(EXAMPLE1_OBJS) $(LSODA_OBJS) -o vanderpol_demo


plotly_rp_x_return_map_data.js: rp_x_return_map.csv
	python ../tools/csv_to_plotly.py rp_x_return_map.csv scatter > plotly_rp_x_return_map_data.js

rp_x_return_map.csv: rp.csv rp_convert_to_return_map_format.py
	python rp_convert_to_return_map_format.py

rp.csv: rossler_pmap
	./rossler_pmap > rp.csv

rossler_pmap: $(EXAMPLE2_OBJS) $(LSODA_OBJS)
	gfortran $(EXAMPLE2_OBJS) $(LSODA_OBJS) -o rossler_pmap


%.o: %.f
	gfortran -std=legacy -c $<

$(VFGEN_EXAMPLE1_OUTPUT): ../example_vf/vanderpol.vf
	vfgen lsoda:demo=yes ../example_vf/vanderpol.vf

$(VFGEN_EXAMPLE2_OUTPUT): ../example_vf/rossler.vf
	vfgen lsoda:func=yes ../example_vf/rossler.vf

clean:
	rm -f *.o rossler_pmap vanderpol_demo rp.csv vdp.csv

purge: clean
	rm -f $(ALL) *.o rossler_pmap vanderpol_demo
