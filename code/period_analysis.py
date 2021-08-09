import numpy as np
from wavelet import *

LCs = ['temperature', 'vlos', 'vturb', '$n_e$']
data_folder = '/home/efredborg/Documents/summer_project2021/data_files/'
data = np.loadtxt(data_folder+'vars.dat')
for i, LC_name in enumerate(LCs):
    LC = data[:,i]
    wavelet_func(LC, LC_type = LC_name, plot_LC=True, P_max = 60)
    #fourier(LC, LC_type= LC_name, P_max = 32)
