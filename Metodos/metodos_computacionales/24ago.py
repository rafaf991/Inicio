
import scipy.integrate as integrate
import matplotlib.pyplot as plt

valorreal = (1.0/8)
errorgrafx =[]
errorgrafy =[]
def integrar_trapecio(func,a,b,error):
	"""
     	    >>> abs(integrar_trapecio(polinomiox7,0,1,0.001)- 1.0/8)< 0.001
	    True
      	    
    	"""

	
	suma = 0
	n = 10
	while abs(suma -valorreal) > error :
		suma = 0
		interval = float((a-b)*1.0/n)
		for i in range (0,n+1):
			if(i == 0 ):
				suma+=interval*float(func(a+interval*i)/2)

			else: suma+=interval*func(a+float(interval*i))
		
			if (abs(suma+interval*func(a+float(interval*(i))/2) -valorreal)< error):
				suma+=interval*func(a+float(interval*(i)))/2
    				errorgrafx.append(n)
				errorgrafy.append(abs(suma - valorreal))				
				return suma
			
		
		errorgrafx.append(n)
	        errorgrafy.append(abs(suma - valorreal))	
		n += 1
	return suma


def polinomiox7 (x):
	return x**7


print "el valor real es :", valorreal
print integrar_trapecio(polinomiox7,0,1,0.01)
plt.plot(errorgrafx,errorgrafy)
plt.semilogy()
plt.semilogx()
plt.show()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
