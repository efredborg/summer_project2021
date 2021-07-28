import numpy as np
import pyreadstat
import pywt
import matplotlib.pyplot as plt

x = [3,7,1,1,-2,5,4,6]

cA, cD = pywt.dwt(x, 'haar') # wavelet transform
y = pywt.idwt(cA, cD, 'haar') # Inverse wavelet transform
print(cA) # approximation coeffs
print(cD) # detailed coeffs
print(y) # reconstructed signal
