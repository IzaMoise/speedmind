import os
import pymodis
from pymodis import downmodis
from pymodis import parsemodis
import glob

dest = "/Users/iza/Desktop/modis_data"
tiles="h18v04,h19v04"
day="2014-08-14"
delta=1

modisDown = downmodis.downModis(destinationFolder=dest, tiles=tiles, today=day, delta=delta)
modisDown.connect()

modisDown.downloadsAllDay()

files = glob.glob(os.path.join(dest, 'MOD11A1.A2014*.hdf'))
print(files)

