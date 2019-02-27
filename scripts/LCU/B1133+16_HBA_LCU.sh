#!/bin/bash

# generated with generateLCUScript.py

rspctl --bitmode=8

/opt/lofar/bin/beamctl --antennaset=HBA_JOINED --rcus=0:191 --band=110_190 --beamlets=0:487 --subbands=12:499 --anadir=3.037109,0.276656,J2000 --digdir=3.037109,0.276656,J2000 &
