#!/bin/bash

# generated with generateObsScripts.py on 2019-03-14 21:16:43.599194

# lane 3
/home/artemis/lump/lump/bin/Basic_LuMP_Recorder.py --port=UDP:16082 --clock_speed=200 --beamlets_per_lane=122 --datadir=/local_data/ARTEMIS/20190314_211643_B1133+16 --data_type_in=L_intComplex16_t --station_name=UK608 --writer_type=LuMP1 --physical_beamlet_array=[244:366] --rcumode_array=[5]*122 --epoch_array=[J2000]*122 --verbose --duration=60 --subband_array=[255:377] --filename_base=B1133+16_lane3 --sourcename_array=[B1133+16]*122 --rightascension_array=[3.037109.6]*122 --declination_array=[0.276656.6]*122 --recorder_num_cores=2 
