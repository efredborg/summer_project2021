import numpy as np
import matplotlib.pyplot as plt
import pywt

P = np.array((0.1,32))
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

periods = 1/freq/60 # in minutes
print('periods',periods[0], periods[-1])

#plt.matshow(coefs)
#plt.show()

#print(coefs.shape, freq.shape)

#print(1/freq[0]/60, 1/freq[-1]/60)
plt.figure(figsize=(9,9))
plt.title('Wavelet analysis on siint_400 light curve')
plt.imshow(abs(coefs), aspect='auto', extent = [0,T/60, periods[-1], periods[0 ]])
plt.hlines(8,0, T/60, colors='red',lw=0.8 , label='Expected ~8 min period')
plt.gca().invert_yaxis()
plt.colorbar()
plt.xlabel('obs. time (min.)')
plt.ylabel('Signal period (min.)')
plt.legend()
plt.show()

plt.figure(figsize=(9,9))
plt.plot(np.arange(0,T+dt,dt)/60,signal, lw=0.8 )
plt.show()
