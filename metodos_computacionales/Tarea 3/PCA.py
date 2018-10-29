import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dat =np.genfromtxt("WDBC.dat", delimiter=",", dtype="|U5", autostrip=True)

#Datos sin B o M
print dat, dat.shape[0],dat.shape[1]
datos=np.array(np.zeros([dat.shape[0],dat.shape[1]-2]))
datos[:,:] = dat[:,2:]

for i in range(dat.shape[0]):
    if (dat[i,1]=="M"):
        dat[i,1]=1
    else: dat[i,1]=0
k=np.copy(dat)

#mean
mean=np.zeros(datos.shape[1])
for i in range(datos.shape[1]):
    a=0
    for j in range(dat.shape[0]):
        a+=datos[j,i]
    a=a/dat.shape[0]
    datos[:,i]-=a

#varianza
var=np.zeros(datos.shape[1])
for i in range(datos.shape[1]):
    a=0
    for j in range(dat.shape[0]):
        a+=(datos[j,i])**2
    a=a/dat.shape[0]
    datos[:,i]=datos[:,i]/np.sqrt(a)
#covarianza

cov=np.zeros([datos.shape[1],datos.shape[1]])

for i in range(datos.shape[1]):
    for j in range(datos.shape[1]):
        a=0
        for k in range(datos.shape[0]):
            a+=(datos[k,i]*datos[k,j])
        a=a/dat.shape[0]
        cov[j][i]=a


eigenvalues,eigenvectors=np.linalg.eig(cov)
vectors=[]
for i in eigenvectors:
    b=[]
    for j in i:
        c="%2.2f"  %j
        b.append(float(c))
    vectors.append(b)

for i in range(len(eigenvalues)):
    print "Dato: %s ,Eigenvalue: %2.2f Eigenvector: %s" %(i+1,eigenvalues[i],vectors[i])
    print " "
print "Los parametros mas importantes son:"
for i in range (len(eigenvalues)):
    if (eigenvalues[i]>1):
        print "Dato: %s, Eigenvalue: %s " %(i+1,eigenvalues[i])
print "El ID y el diagnostico no se cuentan aqui"

#Proyeccion
vectors1=np.copy(eigenvectors)
print eigenvalues[0],eigenvalues[1]

pc1=vectors1[0]
pc2=vectors1[1]
vectorspc1=[]
vectorspc2=[]
vectorsM=[]
vectorsB=[]
datos[:,:] = dat[:,2:]
print datos
for i in range(dat.shape[0]):
    if(dat[i,1]=="0"):
        a=np.dot(pc1,datos[i,:])
        b=np.dot(pc2,datos[i,:])
        vectorsB.append([a,b])
    else:
        a=np.dot(pc1,datos[i,:])
        b=np.dot(pc2,datos[i,:])
        vectorsM.append([a,b])
vectorsB=np.array(vectorsB)
vectorsM=np.array(vectorsM)

plt.scatter(vectorsB[:,0],vectorsB[:,1], label="Datos Venigno")
plt.scatter(vectorsM[:,0],vectorsM[:,1],label="Datos Maligno")
plt.legend(loc=0)
plt.show()
