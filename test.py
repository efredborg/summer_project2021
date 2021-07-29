import numpy as np
import pyreadstat
import pywt
import matplotlib.pyplot as plt
from scipy.fftpack import fft





signal = np.loadtxt('siint_400.dat')
dt_min = 37/60 # minutes
dt_sec = 37 # seconds
N = len(signal)
T = (N-1)*dt_min
fs = 1/T*60
t = np.linspace(0,dt_min*N,N)

def wavelet_transform(t,signal,wa,k):
    yf=fft(signal)
    w=np.linspace(0,fs,N)
    wave=2*(np.exp(-(k*(w-wa)/wa)**2)-np.exp(-k**2)*np.exp(-(k*w/wa)**2))
    return yf*wave


def wavelet_diagram(signal,K):
    wa=np.linspace(800,2000,1201)
    wa = np.linspace(0.03,2, 2000) # frequencies explored
    inv_wave=[]
    for i in range(len(wa)):
        wave=wavelet_transform(t,signal,wa[i],K)
        inv_wave.append(np.abs(np.fft.ifft(wave)))
    inv_wave=np.array((inv_wave))
    plt.contourf(t,1/wa,inv_wave);plt.colorbar();
    plt.title('Wavelet diagram with \n wave number K=%g' % K)

    #plt.show()

plt.figure(figsize=(13,13))
plt.subplot(221)
wavelet_diagram(signal, 50)
plt.ylabel('Period in minutes')

plt.subplot(222)
wavelet_diagram(signal, 25)

plt.subplot(223)
wavelet_diagram(signal, 12)
plt.xlabel('Time (min.)')
plt.ylabel('Period in minutes')

plt.subplot(224)
wavelet_diagram(signal, 6)
plt.xlabel('Time (min.)')

plt.show()



'''x = [3,7,1,1,-2,5,4,6]

cA, cD = pywt.dwt(x, 'haar') # wavelet transform
y = pywt.idwt(cA, cD, 'haar') # Inverse wavelet transform
#print(cA) # approximation coeffs
#print(cD) # detailed coeffs
#print(y) # reconstructed signal


signal = np.loadtxt('siint_400.dat')

cA, cD = pywt.dwt(signal,'haar')

print(cA.shape, cD.shape)
y = pywt.idwt(cA, cD, 'haar')

tx = np.arange(0,len(signal),1)
plt.plot(tx, signal, lw=0.8, label = 'signal')
plt.plot(tx, y, lw=0.8, ls='dashed', label='inv signal')'''

'''plt.show()

error = np.abs(signal-y)
print(np.max(error))
print(np.sum(error))'''
