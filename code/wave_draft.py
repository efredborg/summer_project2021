import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.fftpack import fft, fftfreq
plt.rcParams['font.size'] = 16
save_folder = 'plots/'

P = np.array((0.1,32)) # period interval we wish to consider (minutes)
P_sec = P*60
F_sec = 1/P_sec


dt = 37 # seconds
N = 660
T = (N-1)*dt
# scales translates to frequency or period. 6500 is around 130min period. 1700 is around 34min
# 4000 is 82 min
scales = np.arange(1,180) #

def wavelet(signal, LC_type = '', plot_LC=False, show=False):
    signal = signal-(np.cumsum(signal)/np.arange(1,len(signal)+1)) # subtracting the running average
    #signal = signal - np.mean(signal)
    signal = signal/np.std(signal) # detrending the light curve
    coefs, freq = pywt.cwt(signal, scales, 'morl', sampling_period = dt)
    periods = 1/freq/60 # in minutes
    print('periods',periods[0], periods[-1])

    plt.figure(figsize=(9,9))
    plt.title('Wavelet analysis on %s light curve' % LC_type)
    plt.imshow(np.abs(coefs)**2, aspect='auto', extent = [0,T/60, periods[-1], periods[0 ]],  cmap=plt.cm.seismic)
    #plt.hlines(8,0, T/60, colors='red',lw=0.8 , label='Expected ~8 min period')
    plt.gca().invert_yaxis()
    plt.colorbar()
    plt.xlabel('obs. time (min.)')
    plt.ylabel('Signal period (min.)')
    #plt.legend()
    plt.savefig(save_folder+'wavelet_%s.png' % LC_type)
    if show==True:
        plt.show()
    if plot_LC==True:
        plt.figure(figsize=(9,9))
        plt.title('Light curve of %s' % LC_type)
        plt.plot(np.arange(0,T+dt,dt)/60,signal, lw=0.8 )
        plt.xlabel('Obs. time (min.)')
        plt.ylabel('Amplitude, %s' % LC_type)
        plt.savefig(save_folder+'LC_%s.png' % LC_type)
        if show==True:
            plt.show()



#LC_type is name of light curve type or variable name.
# P_max is max period evaluated
def fourier(signal, LC_type = '', P_max=130, show=False):
    yf=np.flip(fft(signal)[0:N//2]) # flipped to match period
    np.seterr(divide='ignore') # ignore the divide by zero warning caused in the next line
    xp=np.flip(1/fftfreq(N, dt)[:N//2]/60) # period in minutes, flipped to go from small to large
    indx = np.where(xp<=P_max)[0][-1]
    yf = yf[:indx+1] # +1 to include endpoint
    xp = xp[:indx+1]


    plt.figure(figsize=(9,9))
    plt.title('Fourier tranform of %s light curve' % LC_type)
    plt.plot(xp[:indx],2.0/N * np.abs(yf[:indx]), c='k', lw=0.8)
    plt.xlabel('Period (min.)')
    plt.ylabel('Amplitude')
    plt.savefig(save_folder+'fft_%s' % LC_type)
    if show==True:
        plt.show()

if __name__ == "__main__":
    siint400 = np.loadtxt('data_files/siint_400.dat')
    wavelet(siint400, LC_type = 'siint400', )
    #fourier(siint400, LC_type= 'siint400', P_max = 15)
