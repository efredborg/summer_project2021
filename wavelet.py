import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.fftpack import fft, fftfreq

siint400 = np.loadtxt('siint_400.dat')

P = np.array((0.1,32)) # period interval we wish to consider (minutes)
P_sec = P*60
F_sec = 1/P_sec


dt = 37 # seconds
dt_min = dt/60
N = 660
T = (N-1)*dt
T_min = T/60
scales = np.arange(1,1700)

def wavelet(signal, LC_type = '', plot_LC=False):
    coefs, freq = pywt.cwt(signal, scales, wavelet = 'morl')
    periods = 1/freq/60 # in minutes
    #print('periods',periods[0], periods[-1])

    plt.figure(figsize=(9,9))
    plt.title('Wavelet analysis on %s light curve' % LC_type)
    plt.imshow(abs(coefs), aspect='auto', extent = [0,T/60, periods[-1], periods[0 ]])
    #plt.hlines(8,0, T/60, colors='red',lw=0.8 , label='Expected ~8 min period')
    plt.gca().invert_yaxis()
    plt.colorbar()
    plt.xlabel('obs. time (min.)')
    plt.ylabel('Signal period (min.)')
    plt.legend()
    plt.show()
    if plot_light_curve==True:
        plt.figure(figsize=(9,9))
        plt.title('Light curve of %s' % LC_type)
        plt.plot(np.arange(0,T+dt,dt)/60,signal, lw=0.8 )
        plt.xlabel('Obs. time (min.)')
        plt.ylabel('Amplitude, %s' % LC_type)
        plt.show()

#wavelet(siint400)

def fourier(signal, LC_type = '', P_max=None):
    yf=np.flip(fft(signal)[0:N//2])
    xp=np.flip(1/fftfreq(N, dt)[:N//2]/60) # period in minutes
    print(len(xp), len(yf))
    #indx = np.where(xp<=35)[0][-1]
    if P_max =! None:
        indx = np.where(xp<=P_max)[0][-1]
        yf = yf[:indx]
        xp = xp[:indx]
        

    plt.figure(figsize=(9,9))
    plt.title('Fourier tranform of %s light curve' % LC_type)
    plt.plot(xp[:indx],2.0/N * np.abs(yf[:indx]), c='k', lw=0.8)
    #plt.plot()
    plt.show()

fourier(siint400, LC_type= 'siint400')
