import numpy as np
import matplotlib.pyplot as plt


dat=np.genfromtxt("graf3.txt",delimiter="  ")
print dat
plt.plot(dat[:,0],dat[:,1])
plt.show()
plt.clf()
plt.plot(dat[:,0],dat[:,2])
plt.show()
plt.clf()
plt.plot(dat[:,0],dat[:,3])
plt.show()
plt.clf()
plt.plot(dat[:,0],dat[:,4])
plt.show()
plt.clf()
plt.plot(dat[:,1],dat[:,3])
plt.show()
