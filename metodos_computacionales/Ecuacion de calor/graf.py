import numpy as np
import matplotlib.pyplot as plt

dat=np.genfromtxt("eccalor.txt",delimiter= " ")

plt.imshow(dat[:,:])
plt.colorbar()
plt.plot()
plt.show()
