#!/bin/bash

# generated with generateLuMPScript.py

# lane 1
/home/artemis/lump-lofar-und-mpifr-pulsare/lump/bin/Basic_LuMP_Recorder.py --port=UDP:16080 --clock_speed=200 --beamlets_per_lane=122 --datadir=/local_data/ARTEMIS/20190226_B1133+16 --data_type_in=L_intComplex16_t --station_name=UK608 --writer_type=LuMP1 --physical_beamlet_array=[0:122] --rcumode_array=[5]*122 --epoch_array=[J2000]*122 --verbose --duration=3600 --subband_array=[111:133] --filename_base=B1133+16_lane1 --sourcename_array=[B1133+16]*122 --rightascension_array=[3.037109]*122 --declination_array=[0.276656]*122 --recorder_num_cores=2 
