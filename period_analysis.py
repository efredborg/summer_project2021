import numpy as np
from wavelet import *

LCs = ['temperature', 'vlos', 'vturb', '$n_e$']
data_folder = 'data_files/'
data = np.loadtxt(data_folder+'vars.dat')
#data = np.loadtxt(data_folder+'siint_400.dat')
#wavelet(data, LC_type = 'siint400')
#fourier(data, LC_type = 'siint400', P_max = 32)
#temp = data[:,0]
#wavelet(temp, LC_type = 'temperature')
#fourier(temp, LC_type= 'temperature', P_max = 32)
for i, LC_name in enumerate(LCs):
    LC = data[:,i]
    wavelet(LC, LC_type = LC_name)
    fourier(LC, LC_type= LC_name, P_max = 32)
