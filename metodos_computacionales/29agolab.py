import sys
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random
N = sys.argv
intervalo =[-1,1]
nintervalo = np.linspace(intervalo[0],intervalo[1],100000)
def pol(x):
   return (35*(x**4)-30*(x**2)+3)/8.0
print N
x = np.linspace(-1,1,N[1])
y= pol(x)

plt.plot(x,y,label="$35*x**4-30*x**2+3$")
plt.legend(loc=0)
#def analitica
analitica = 0
print analitica
val =pol(x)
def separarfunciones(func):
	positivo = []
	xpos=[]
	negativo =[]
	xneg =[]	
	for i in range (len(func)):
		if func[i] <= 0:
			positivo.append(func[i])
			negativo.append(0)
			
		
		else :
			negativo.append(func[i])
			positivo.append(0)
  
	return xpos,xneg ,positivo,negativo

xpos,xneg,pos,neg = separarfunciones(pol(x))
plt.plot(x,pos,label="$35*x**4-30*x**2+3$")
plt.legend(loc=0)
plt.plot(x,neg,label="$35*x**4-30*x**2+3$")
plt.legend(loc=0)
plt.show()

#montecarlo


min_y = 0.0
max_y = max(pos)
max_x = intervalo[1]
min_x =intervalo[0]
print max_x
print min_x
n_random = int(N[1])
print n_random
random_x = random.rand(n_random) * (max_x - min_x) + min_x
random_y = random.rand(n_random) * (max_y - min_y) + min_y
delta = pol(random_x) - random_y
below  = np.where(delta>0.0)
plt.scatter(random_x[below], random_y[below])
interval_integral = (max_y-min_y) * (max_x - min_x)
integral  = interval_integral * (size(below)/(1.0*size(random_y)))
print integral

