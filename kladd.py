import numpy as np
import pyreadstat
import pywt
import matplotlib.pyplot as plt
from scipy.fftpack import fft

x = np.arange(10)
y = x**2

plt.plot(x, y)
plt.savefig('plots/fig.png')
