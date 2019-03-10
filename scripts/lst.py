#!/usr/bin/env python3

import astropy.time
import astropy.coordinates

locUK608 = astropy.coordinates.EarthLocation.from_geodetic(lat=51.143833512, lon=-1.433500703, height=176.028) # UK608 LBA
locIE613 = astropy.coordinates.EarthLocation.from_geocentric(3801633.528060000, -529021.899396000, 5076997.185, unit='m') # IE613 LBA

import argparse
parser = argparse.ArgumentParser(
    description='''Print the UTC and LST for an observatory''')
parser.add_argument('-o', '--observatory', help='Observatory name, default: UK608', default='UK608')
args = parser.parse_args()

t = astropy.time.Time.now()

if args.observatory.startswith('UK608'): t.location = locUK608
elif args.observatory.startswith('IE613'): t.location = locIE613

lst = t.sidereal_time('mean')

print('Observatory:', args.observatory, t.location.to_geodetic())
print('UTC: ', t)
print('LST: ', lst)

