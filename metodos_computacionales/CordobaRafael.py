import numpy as np



def resolv(A,b):
	A = np.array(A)
	b = np.array(b)
	c = np.concatenate((A,b.T), axis = 1)
	m,n = np.shape(c)
	print c
	for i in range (0,m):
		for j in range(i+1,m):		
			c[j,:] =c[j,:]-float(c[j,i])*c[i,:]/float(c[i,i])
			
	return c




Ax =[[1,3,5],[3,5,3],[2,4,5],[1,3,5]]
b =[[4,2,3,1]]

print resolv(Ax,b)

#Bono

A=[1,3,4,5,56,6,7,8]
for j in range(0,len(A)):
        for i in range(j,len(A)):
            if A[i]>A[j]:
            	A[i],A[j] =A[j],A[i]


def resolvbono1(A,b):
	A = np.array(A)
	b = np.array(b)
	c = np.concatenate((A,b.T), axis = 1)
	m,n = np.shape(c)
	
	for j in range(0,m):
        		for i in range(j,m):
            			if c[i,0]>c[j,0]:
            				c[[i,j]] = c[[j,i]]
	print c
	for i in range (0,m):
		for j in range(i+1,m):		
			c[j,:] =c[j,:]-float(c[j,i])*c[i,:]/float(c[i,i])
		
		for k in range(i+1,m):
        		for l in range(k,m):
            			if c[l,l]>c[k,k]:
            				c[[l,k]] = c[[k,l]]
		

#Bono2

def resolverecuacion(A):
	m= np.shape(A)[0]
	x=[]
	for i in range(0,m):
		r =A[i,-1]
		for j in range(0,i):
			r += -x[j]*A[i,j]
		x.append(r)
print x[-1:0]

