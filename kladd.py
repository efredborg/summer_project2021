import numpy as np
import pyreadstat
import pycwt as wavelet
import matplotlib.pyplot as plt
from scipy.fftpack import fft

signal = np.loadtxt('data_files/siint_400.dat')
scales = np.arange(1,1700)

signal = signal-(np.cumsum(signal)/np.arange(1,len(signal)+1)) # subtracting the running average
signal = signal/np.std(signal) # detrending the light curve
dt = 37/60 # minutes
N = 660
T = (N-1)*dt

s0 = 2*dt
dj = 1/12
J = 3.5/dj # includes periods up to 132 minutes
#alpha, _, _ = pywt.ar1(dat)
mother = wavelet.Morlet(2   q)

wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(signal, dt, dj, s0, J,mother)
periods = 1/freqs # in minutes
print(wave.shape)
#print(1/freqs)
plt.imshow(np.abs(wave)**2, aspect='auto', extent = [0,T, periods[-1], periods[0]], cmap=plt.cm.seismic)
plt.show()
#coefs, freq = pywt.cwt(signal, scales, wavelet = 'morl')
