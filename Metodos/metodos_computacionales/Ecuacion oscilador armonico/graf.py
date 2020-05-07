import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("graf.txt", delimiter="  ")
datos2 = np.genfromtxt("graf2.txt", delimiter="  ")
datos3= np.genfromtxt("graf3.txt",delimiter="  ")
t=datos[:,0]
x=datos[:,1]
v=datos[:,2]
plt.plot(t,x,label ="metodo euler")
plt.plot(t,np.sin(np.sqrt(3)*t)/np.sqrt(3),label="real")
plt.plot(t,v,label ="metodo velocidad")
plt.plot(t,np.cos(np.sqrt(3)*t),label="real")
plt.legend(loc=0)
plt.savefig("xt.png")
plt.clf()
