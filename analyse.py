import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
data = np.loadtxt('vars.dat')

dt_min = 37/60 # minutes
dt_sec = 37 # seconds
N = data.shape[0]
t = np.linspace(0,dt_min*N,N)

max_eval_t = 80 # minutess
ind = np.where(t<max_eval_t)[0][-1]
t = t[0:ind]

T = (N-1)*dt_min
fs = 1/T*60
f1 = 8#min
f2 = 50 # min
c1 = 1; c2 = 1.7
def x(t,f1,f2):
    X=c1*np.sin(2*np.pi*f1*t)+c2*np.sin(2*np.pi*f2*t)
    return X

def fourier(signal,t, dt_sec):
    N = len(t)

    yf=fft(data[:,0])
    #yf = fft(x(t,f1,f2))
    #xf = fftfreq(N, dt_sec)[:N//2]*60 # per minute
    xf=np.linspace(0,1/(2*dt_sec),(N)//2)*60

    #plt.plot(np.arange(0,len(xf),1), xf, c='k', lw=0.8)
    #plt.plot(np.arange(0,len(xf2),1), xf2, lw=0.8)
    #plt.show()

    plt.figure(figsize = (14,9))
    plt.subplot(121)
    plt.plot(t, data[:N,0], c = 'k', lw = 0.8)

    plt.subplot(122)
    plt.plot(1/xf[:N],2.0 * np.abs(yf[:int(N/2)]/N), c='k', lw=0.8)
    #plt.plot(2.0 * np.abs(yf[1:int(N//2)]/N), 1/xf[1:], c='k', lw=0.8)




#fourier(x(t, f1, f2), t, dt_sec)
#plt.show()
xf=np.linspace(0,1/(2*dt_sec),(N)//2)*60

plt.plot(xf, xf)
plt.show()
