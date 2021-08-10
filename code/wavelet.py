import numpy as np
import matplotlib.pyplot as plt
import pywt
import pycwt as wavelet
from scipy.fftpack import fft, fftfreq
plt.rcParams['font.size'] = 16
plot_folder = '/home/efredborg/Documents/summer_project2021/plots/'
data_folder = '/home/efredborg/Documents/summer_project2021/data_files/'


def wavelet_func(signal, LC_type = '', plot_LC=False, show=False, P_max = 135):
    #Defining som important quantities
    dt = 37/60 # minutes. Determined by comparing time of obs in consequtive fits files.
    N = 660 # number of data points in the time dimension
    T = (N-1)*dt # Total observation duration given that the first data point is at t=0
    t = np.arange(0,T+dt, dt)
    periods = np.arange(2*dt, P_max+dt, dt) #evaluated periods
    freqs = 1/periods   # corresponding frequencies

    # preparing data for wavelt analysis
    detrend_sig = signal-(np.cumsum(signal)/np.arange(1,len(signal)+1)) # subtracting the running average, detrending
    std = np.std(detrend_sig)
    var = std**2
    norm_sig = detrend_sig/std # normalising with respect to standard deviation

    # performing wavelet anaysis
    wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(norm_sig, dt,wavelet='morlet', freqs=freqs)

    # redefining periods
    periods = 1/freqs
    fft_periods = 1/fftfreqs

    # further analysis on wavelet outputs
    power = np.abs(wave)**2
    #power /= scales[:, None]

    #determining significance levels
    signif, fft_theor = wavelet.significance(norm_sig, dt, scales, significance_level=0.95, wavelet='morlet')
    sig95 = np.ones([1, N]) * signif[:, None]
    sig95 = power / sig95

    glbl_power = np.mean(power, axis=1)
    dof = N-scales
    #glbl_signif, tmp = wavelet.significance(var, dt,scales, 1, significance_level=0.95, dof=dof, wavelet='morlet')

    print('periods',periods[0], periods[-1])
    #print('fft periods',fft_periods[0], fft_periods[-1])


    #collapsing the power in the time dimension, but expluding the area outside the cone of interest
    coi_indx = []
    for i in range(len(coi)):
        indx = np.where(periods<= coi[i])[0]
        if len(indx)<1:
            coi_indx.append(int(0))
        else:
            coi_indx.append(indx[-1])

    collapsed_power = np.zeros((len(periods)))
    for i in range(power.shape[1]):
        collapsed_power += power[:,coi_indx[i]]

    # finding the first and second dominant periods
    #dividing periods into 3 intervals, finding maximum in each, and choosing the two laregst peaks.
    left_indx = np.where(periods<=15)[0][-1]
    left = np.argmax(collapsed_power[:left_indx])
    middle_indx = np.where(periods<=27)[0][-1]
    middle = np.argmax(collapsed_power[left_indx:middle_indx])+left_indx
    right = np.argmax(collapsed_power[middle_indx:])+middle_indx
    #left area=0, middle=1, right=2
    inds = [left, middle, right]
    first = inds[np.argmax(np.array((collapsed_power[inds[0]], collapsed_power[inds[1]], collapsed_power[inds[2]])))]
    inds.remove(first)
    second = inds[np.argmax(np.array((collapsed_power[inds[0]], collapsed_power[inds[1]])))]



    #plottinh the global wavelet power with dominant periods
    plt.figure(figsize=(9,9))
    plt.title('Global power profile for %s light curve' % LC_type)
    plt.plot(periods, collapsed_power, c='k', lw=0.8)
    plt.plot(periods[first], collapsed_power[first],'o', c='red',label='Dominant period, P = %.1f' % periods[first])
    plt.plot(periods[second], collapsed_power[second],'o', c='red',label='Secondary period, P = %.1f' % periods[second])
    plt.xlabel('Periods (min.)')
    plt.ylabel('Amplitude')
    if periods[first]>30:
        plt.legend(loc='lower right')
    else:
        plt.legend(loc='upper right')
    plt.savefig(plot_folder+'glbl_power_p%i_LC_%s.png' % (int(periods[-1]),LC_type))
    #plt.show()

    #plottinhg wavelet power map with cone of influence
    plt.figure(figsize=(9,9))
    plt.title('Wavelet analysis on %s light curve' % LC_type)
    plt.imshow(power, aspect='auto', extent = [0,T, periods[-1], periods[0]], cmap=plt.cm.seismic)
    plt.plot(t, coi, c='r', label='Cone of influence')
    plt.gca().invert_yaxis()
    plt.colorbar()
    plt.xlabel('obs. time (min.)')
    plt.ylabel('Signal period (min.)')
    plt.legend()
    plt.savefig(plot_folder+'wavelet_p%i_%s.png' % (int(periods[-1]), LC_type))
    if show==True:
        plt.show()
    if plot_LC==True:
        plt.figure(figsize=(9,9))
        plt.title('Light curve of %s' % LC_type)
        plt.plot(t,signal, lw=0.8 )
        plt.xlabel('Obs. time (min.)')
        plt.ylabel('Amplitude, %s' % LC_type)
        plt.savefig(plot_folder+'LC_%s.png' % LC_type)
        if show==True:
            plt.show()


    # plotting the fft but only including up to the max period evaluated
    fft_power = np.abs(fft)**2
    fft_periods = np.flip(fft_periods)
    fft_power = np.flip(fft_power)
    indx = np.array((np.where(fft_periods <= P_max)))[0,-1]
    fft_periods = fft_periods[:indx+1]
    fft_power = fft_power[:indx+1]
    plt.figure(figsize=(9,9))
    plt.title('Fourier tranform of %s light curve' % LC_type)
    plt.plot(fft_periods, fft_power, lw=0.8, c='k')
    plt.xlabel('Period (min.)')
    plt.ylabel('Amplitude')
    plt.savefig(plot_folder+'fft_p%i_LC_%s'% (int(periods[-1]), LC_type))


if __name__ == "__main__":
    siint400 = np.loadtxt(data_folder + 'siint_400.dat')
    wavelet_func(siint400, LC_type = 'siint400' )
