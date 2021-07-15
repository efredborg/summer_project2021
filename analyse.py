import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('vars.dat')

plt.figure(figsize = (9,9))
plt.plot(np.arange(data.shape[0]), data[:,0], c = 'k', lw = 0.8)
#plt.show()
