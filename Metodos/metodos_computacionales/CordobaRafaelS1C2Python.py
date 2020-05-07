a = 2
b = 2.4

print "la primera tiene un valor de %r y la segunda variable tiene un valor de %r" %(a,b)
c = b**2
print "El resultado es %r" %(c)
lista = ["azul","rio",30,28]
print lista
lista.append(237)
for i in lista:
    print i
lista.pop(1)
print lista
print "la longitud de la lista es %r" %(len(lista))

#Ejercico iteracion

nombres = ['enero', 'febrero', 'marzo', 'abril', 'mayo']

d = dict()

for i in range(0,len(nombres)):
    d[i+1] = nombres[i]

print d
