import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.fftpack import fft

dt = 37
x = np.arange(0, 659*dt,dt)
N = len(x)

P = 8*60
a = 2*np.pi/P
y = np.sin(x*a)
print(2*np.pi/a/60)

'''plt.plot(x, y)
plt.plot(0, 0, 'o')
plt.plot(P, 0, 'o')
print(P/60)
print(1/P*60)
plt.show()'''
f = 1/P
scales = np.arange(1,1700)
coefs, freq = pywt.cwt(y, scales, wavelet = 'morl')
periods = 1/freq/60 # in minutes
print(periods[0], periods[-1])

#plt.matshow(coef)
plt.figure(figsize= (9,9))
plt.imshow(np.abs(coefs), aspect='auto', extent = [0,x[-1], periods[0], periods[-1]])
plt.hlines(P/60, x[0], x[-1], colors='red')
plt.gca().invert_yaxis()
plt.show()


'''yf=fft(y)
xf=np.linspace(0,1/(2*dt),(N)//2)
plt.plot(1/xf/60,2.0 * np.abs(yf[0:int(N//2)]/N))
plt.show()'''

'''P = np.array((0.1,32))
P_sec = P*60
F_sec = 1/P_sec

signal = np.loadtxt('siint_400.dat')
dt = 37 # seconds
dt_min = dt/60
N = len(signal)
T = (N-1)*dt
T_min = T/60
scales = np.arange(1,1700)

coefs, freq = pywt.cwt(signal, scales, wavelet = 'morl')

#plt.matshow(coefs)
#plt.show()

print(coefs.shape, freq.shape)

#print(1/freq[0]/60, 1/freq[-1]/60)
plt.figure(figsize=(9,9))
plt.imshow(abs(coefs), aspect='auto', extent=[0,T,1700,1])
plt.gca().invert_yaxis()
plt.colorbar()
#plt.show()'''
