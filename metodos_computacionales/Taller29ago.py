import numpy as np
import matplotlib.pyplot as plt
def derivada(func,x,h,metodo="FD"):
   if metodo == "FD":
	return (func(x+h) - func(x))/(h*1.0)
   elif metodo == "CD":
	return (func(x+h/2.0) - func(x-h/2.0))/(h*1.0)
   elif metodo == "ED":
	return (8.0*(func(x+h/4.0) - func(x-h/4.0))- (func(x+h/2.0) - func(x-h/2.0))  )/(h*3.0)
   else: return "No es valido el metodo escogido"

def cosquad(x):
	return np.cos(x)**2
def dercos(x):
	return -np.sin(2.0*x)

h= np.linspace(10**(-1),10**(-10),1000)
analitica = dercos(1)
eFD = derivada(cosquad,1,h)-analitica
eCD = derivada(cosquad,1,h,"CD")-analitica
eED = derivada(cosquad,1,h,"ED")-analitica
FD = derivada(cosquad,1,h)
CD = derivada(cosquad,1,h,"CD")
ED = derivada(cosquad,1,h,"ED")
plt.plot(h,100.0*abs(eFD/(1.0*analitica)),color = "red",label = "FD")
plt.legend(loc=0)
plt.plot(h,100.0*abs(eCD/(1.0*analitica)), color ="blue",label = "CD")
plt.legend(loc=0)
plt.plot(h,100.0*abs(eED/(1.0*analitica)),color = "green", label = "ED")
plt.legend(loc=0)
plt.semilogy()
plt.semilogx()
plt.show()

