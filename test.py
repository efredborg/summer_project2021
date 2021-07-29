import numpy as np
import pyreadstat
import pywt
import matplotlib.pyplot as plt
from scipy.fftpack import fft

per_min = np.array((33,0.5))
per_sec = per_min*60
freq_min = 1/per_min
freq_sec = 1/per_sec

wa_test = np.linspace(0.03,2,2000) # frequencies
print(1/wa_test[0], 1/wa_test[-1])

print(freq_min, freq_sec)



signal = np.loadtxt('siint_400.dat')
dt_min = 37/60 # minutes
dt_sec = 37 # seconds
N = len(signal)
T_min = (N-1)*dt_min
T_sec = (N-1)*dt_sec

fs = N/T_sec
t = np.linspace(0,T_min,N)

def wavelet_transform(t,signal,wa,k):
    yf=fft(signal)
    w=np.linspace(0,fs,N)
    wave=2*(np.exp(-(k*(w-wa)/wa)**2)-np.exp(-k**2)*np.exp(-(k*w/wa)**2))
    return yf*wave


def wavelet_diagram(signal,K):
    wa=np.linspace(800,2000,1201)
    wa = np.linspace(freq_min[0], freq_min[1],2000) # frequencies explored in Hz
    inv_wave=[]
    for i in range(len(wa)):
        wave=wavelet_transform(t,signal,wa[i],K)
        inv_wave.append(np.abs(np.fft.ifft(wave)))
    inv_wave=np.array((inv_wave))
    plt.contourf(t,1/wa,inv_wave);plt.colorbar();
    plt.title('Wavelet diagram with \n wave number K=%g' % K)

    # plt.show()

plt.figure(figsize=(13,13))
plt.subplot(221)
wavelet_diagram(signal, 50)
plt.ylabel('Period in minutes')

plt.subplot(222)
wavelet_diagram(signal, 25)

plt.subplot(223)
wavelet_diagram(signal, 20)
plt.xlabel('Time (min.)')
plt.ylabel('Period in minutes')

plt.subplot(224)
wavelet_diagram(signal, 15)
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
