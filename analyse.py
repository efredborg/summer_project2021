import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('vars.dat')

plt.figure(figsize = (9,9))
plt.plot(np.arange(data.shape[0]), data[:,0], c = 'k', lw = 0.8)
#plt.show()

#t0 = 11:47:58.850
#t1 = 11:48:36.100

t0 = 47 + 58.850/60
t1 = 48 + 36.1/60
delta_t = t1-t0
print(delta_t*659/60)


#t659 =
