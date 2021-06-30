import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
filename = 'iris_l2_20140521_114758_3820258168_raster_t000_r00487.fits'

hdu = fits.open(filename)
hdu.info()
