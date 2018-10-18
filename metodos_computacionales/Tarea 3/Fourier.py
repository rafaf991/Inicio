import numpy as np
import matplotlib.pyplot as plt


signal=np.genfromtxt("signal.dat",delimiter =",")
incompletos=np.genfromtxt("incompletos.dat",delimiter =",")


plt.plot(signal[:,0],signal[:,1],label= "Datos signal")
plt.legend(loc=0)
plt.savefig("CordobaRafael_signal.pdf")
