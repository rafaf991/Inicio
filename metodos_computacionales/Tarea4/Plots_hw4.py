import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import math

datcalor= np.genfromtxt("Eccalor.txt",delimiter=" ")
datmovim= np.genfromtxt("graf3.txt",delimiter=" ")


a=[45,10,20,30,40,50,60,70]
for i in range (8):
    dat45=datmovim[1000*i:999*(i+1),:];
    nombre="Trayectoria",a[i]," grados"
    plt.scatter(dat45[:,1],dat45[:,0],label=str(nombre))
    plt.legend(loc=0)
    plt.show()





dat1=datcalor[:,0::3]
dat2=datcalor[:,1::3]
dat3=datcalor[:,2::3]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x=np.linspace(0,50,len(dat1[0,:]))
y=np.linspace(0,50,len(dat1[0,:]))
plt.title("Condiciones iniciales")
ax.scatter(x,y,dat1[0,:], c='r', marker='o')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')

plt.savefig("Condiciones iniciales.pdf")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x=np.linspace(0,50,len(dat1[-1,:]))
y=np.linspace(0,50,len(dat1[-1,:]))
plt.title("Condiciones finales")
ax.scatter(x,y,dat1[-1,:], c='r', marker='o')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')

plt.savefig("Condiciones finales.pdf")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x=np.linspace(0,50,len(dat1[0,:]))
y=np.linspace(0,50,len(dat1[0,:]))
plt.title("Condiciones mitad")
ax.scatter(x,y,dat1[int(math.floor(len(dat1)/2)),:], c='r', marker='o')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')

plt.savefig("Condiciones mitad.pdf")
