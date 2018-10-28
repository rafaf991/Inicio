import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dat =np.genfromtxt("WDBC.dat", delimiter=",", dtype="|U5", autostrip=True)
#Datos sin B o M
print dat, dat.shape[0],dat.shape[1]
datos=np.array(np.zeros([dat.shape[0],dat.shape[1]-1]))
datos[:,1:] = dat[:,2:]
datos[:,0]=dat[:,0]


#mean
mean=np.zeros(dat.shape[1]-1)
for i in range(dat.shape[1]-1):
    a=0
    for j in range(dat.shape[0]):
        a+=datos[j,i]
    a=a/dat.shape[0]
    datos[:,i]-=a

#varianza
var=np.zeros(dat.shape[1]-1)
for i in range(dat.shape[1]-1):
    a=0
    for j in range(dat.shape[0]):
        a+=(datos[j,i])**2
    a=a/dat.shape[0]
    datos[:,i]=datos[:,i]/np.sqrt(a)
#covarianza

cov=np.zeros([dat.shape[1]-1,dat.shape[1]-1])

for i in range(dat.shape[1]-1):
    for j in range(dat.shape[1]-1):
        a=0
        for k in range(dat.shape[0]):
            a+=(datos[k,i]*datos[k,j])
        a=a/dat.shape[0]
        cov[j][i]=a


eigenvalues,eigenvectors=np.linalg.eig(cov)
for i in range(len(eigenvalues)):
    print "Eigenvalue: %s Eigenvector: %s" %(eigenvalues[i],eigenvectors[i])
plt.imshow(np.transpose(datos))
plt.show()
