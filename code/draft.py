import numpy as np
import pyreadstat
import pywt
import pycwt as wavelet
import matplotlib.pyplot as plt
from scipy.fftpack import fft

data_folder = '/home/efredborg/Documents/summer_project2021/data_files/'
#data_folder = '/data_files/'


signal = np.loadtxt(data_folder +'siint_400.dat')
