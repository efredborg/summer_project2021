import numpy as np
import pyreadstat
import pywt
import pycwt as wavelet
import matplotlib.pyplot as plt
from scipy.fftpack import fft




signal = np.loadtxt('data_files/siint_400.dat')
scales = np.arange(1,1700)
dt = 37/60 # minutes
N = 660
T = (N-1)*dt

x = np.arange(0,T+dt,dt)

p = 80
a = 2*np.pi/p
y = np.sin(x*a)


#signal = y-np.mean(y)

#plt.plot(x,y)
#plt.show()


signal = signal-(np.cumsum(signal)/np.arange(1,len(signal)+1)) # subtracting the running average (detrending)
#signal = signal-np.mean(signal)
signal = signal/np.std(signal) # normalising with respect to

s0 = 0.5
dj = 1/12
J = 5/dj # includes periods up to 132 minutes
#alpha, _, _ = pywt.ar1(dat)
mother = wavelet.Morlet(1/8)
periods = np.arange(2*dt, (T+dt)/3,dt)
freqs = 1/periods
wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(signal, dt,wavelet='morlet', freqs=freqs)
periods = 1/freqs # in minutes
#print(coi.shape)
#print(1/freqs)



plt.imshow(np.abs(wave)**2, aspect='auto', extent = [0,T, periods[-1], periods[0]], cmap=plt.cm.seismic)
plt.gca().invert_yaxis()

plt.colorbar()
plt.show()
#coefs, freq = pywt.cwt(signal, scales, wavelet = 'morl')

'''LC_type = 'siint400'
signal = signal-(np.cumsum(signal)/np.arange(1,len(signal)+1)) # subtracting the running average
signal = signal/np.std(signal) # detrending the light curve
coefs, freq = pywt.cwt(signal, scales, wavelet = 'morl')
periods = 1/freq/60 # in minutes
plt.figure(figsize=(9,9))
plt.title('Wavelet analysis on %s light curve' % LC_type)
plt.imshow(np.abs(coefs), aspect='auto', extent = [0,T/60, periods[-1], periods[0 ]], cmap='Spectral')
plt.gca().invert_yaxis()
plt.colorbar()
plt.xlabel('obs. time (min.)')
plt.ylabel('Signal period (min.)')

signal = np.loadtxt('data_files/siint_400.dat')


signal = signal-(np.cumsum(signal)/np.arange(1,len(signal)+1)) # subtracting the running average
#signal = signal/np.std(signal) # detrending the light curve
coefs, freq = pywt.cwt(signal, scales, wavelet = 'morl')
periods = 1/freq/60 # in minutes
plt.figure(figsize=(9,9))
plt.title('Wavelet analysis on %s light curve' % LC_type)
plt.imshow(np.abs(coefs), aspect='auto', extent = [0,T/60, periods[-1], periods[0 ]], cmap='Spectral')
plt.gca().invert_yaxis()
plt.colorbar()
plt.xlabel('obs. time (min.)')
plt.ylabel('Signal period (min.)')

signal = np.loadtxt('data_files/siint_400.dat')


#signal = signal-(np.cumsum(signal)/np.arange(1,len(signal)+1)) # subtracting the running average
#signal = signal/np.std(signal) # detrending the light curve
coefs, freq = pywt.cwt(signal, scales, wavelet = 'morl')
periods = 1/freq/60 # in minutes
plt.figure(figsize=(9,9))
plt.title('Wavelet analysis on %s light curve' % LC_type)
plt.imshow(np.abs(coefs), aspect='auto', extent = [0,T/60, periods[-1], periods[0 ]], cmap='Spectral')
plt.gca().invert_yaxis()
plt.colorbar()
plt.xlabel('obs. time (min.)')
plt.ylabel('Signal period (min.)')

plt.show()'''
