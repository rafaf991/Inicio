import random
import math
def lanzarhasta100():
    points = 0
    throws = 0
    while points < 100: 
       points += int(random.random()*6)+1
       throws += 1
    return throws

v =[]
for i in range (0, 100):
    v.append(lanzarhasta100())
mean = sum(v)/len(v)
numerotiros = math.ceil(mean)
print ("Se nesecitan en promedio",numerotiros, "tiros en un dado para alcancar 100") 


def distance(a,b):
    distancia = 0
    if len(a) == len(b):
        for i in range (0,len(a)):
            distancia += (a[i]-b[i])**2
    distancia = (distancia)**0.5
    
    return distancia
print (distance([0,0], [1,1]),distance([1,5], [2,2]),distance([0,1,2], [2,3,4]))

#3.1

class Circle:
    def __init__(self, radius):
        self.radius = radius #all attributes must be preceded by "self."
    def area(self):
        import math
        return math.pi * self.radius * self.radius
    def perimeter(self):
        import math
        return 2*math.pi*self.radius

#3.2

class Vector3D:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c
        
    def dot(self,w):
        res =self.x*w.x+self.y*w.y+self.z*w.z
        return res
v = Vector3D(2, 0, 1)
w = Vector3D(1, -1, 3)
v.dot(w)
print (v.dot(w))



#4.1

a=[]
for i in range(0,10):
    a.append(i)
print (a)
random.shuffle(a)
print (a)
    
#1.1 numpy
import numpy as np
a = np.random.rand(4, 8)
a[:,-1] = -1
a[2,:] = 2
print (a)

#1.2 numpy

a=np.random.normal(size=1000)
ii = (a > 2)
print ( "la cantidad de elementos con valor mayor a 2 son =",len(a[ii]))

#1.3

a=np.random.normal(size=1000)
ii = (a < 0)
jj = (a >0)
b = []
for i in a:
    if i>0:
        b.append(-1)
    else:
        b.append(1)
print (b)

#1.4
import numpy as np
import math
import matplotlib.pyplot as plt #


t = np.linspace(-10,10,10000)
plt.figure() 
x = np.sin(5*t)
y = np.cos(4*t)
plt.scatter(x,y) 
plt.show()
