import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
from scipy.interpolate import interp1d

signal=np.genfromtxt("signal.dat",delimiter =",")
incompletos=np.genfromtxt("incompletos.dat",delimiter =",")


plt.plot(signal[:,0],signal[:,1],label= "Datos signal")
plt.legend(loc=0)
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.savefig("CordobaRafael_signal.pdf")
plt.clf()
plt.plot(incompletos[:,0],incompletos[:,1],label= "Datos incompletos")
plt.legend(loc=0)
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.savefig("CordobaRafael_incompletos.pdf")


def fft1(x):

    N=len(x)
    X=[]
    for k in range(0,N):
        sum=0
        for n in range (0,N):
            sum+=x[n]*np.exp(-1j*2*np.pi*(k*n)/N)
        X.append(sum)
    return X

X=fft1(signal[:,1])
N=len(X)
freq=fft.fftfreq(len(X))
freq2=2*np.pi*np.linspace(-N,N,N)/N

#freq,X=zip(*sorted(zip(freq,X)))
#print freq
#print freq2
t=np.linspace(0,len(X),len(X))
plt.clf()
plt.plot(freq,np.abs(X),label="Transformada implementacion propia")
#plt.plot(t,50+np.abs(fft.fft(signal[:,1])),label="Transformada implementacion np.")
plt.legend(loc=0)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Norma de la Transformada")
plt.savefig("CordobaRafael_TF.pdf")
##Frecuancias principaples

where =np.where(np.abs(X)>20)
freq1=np.copy(freq)
transrec=np.copy(X)

where2 =np.where(np.abs(X)<20)
transrec[where2]=0+0j
plt.clf()
plt.plot(freq,np.abs(transrec),label="Transformada sin ruido")
plt.legend(loc=0)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Norma de la Transformada")
#plt.show()
plt.clf()
plt.plot(t,np.real(fft.ifft(transrec)))
plt.savefig("CordobaRafael_filtrada.pdf")




print "Las frecuencias principales son:" ,freq1[where]


print "No se puede aplicar la Transformada a los datos incompletos por que no estan igualemnte espaciados."
cuadratica = interp1d(incompletos[:,0],incompletos[:,1],kind ='quadratic')
cubica = interp1d(incompletos[:,0],incompletos[:,1], kind='cubic')
t=np.linspace(np.amin(incompletos[:,0]),np.amax(incompletos[:,0]),512)
datcub=cubica(t)
datcuad=cuadratica(t)


transfcub=fft1(datcub)
freqcub=fft.fftfreq(len(transfcub))
transfcuad=fft1(datcuad)
freqcuad=fft.fftfreq(len(transfcuad))

plt.clf()
plt.plot(311)

plt.subplot(311)
plt.plot(freqcub, np.abs(transfcub),label="Interpolacion cubica")
plt.legend(loc=0)
plt.subplot(312)
plt.plot(freqcuad, np.abs(transfcuad),label="Interpolacion cuadratica")
plt.legend(loc=0)

plt.subplot(313)
plt.plot(freq,np.abs(X),label="Datos originales" )


plt.legend(loc=0)


plt.savefig("CordobaRafael_TF_interpola.pdf")
plt.clf()




print "Se ve que las graficas interpoladas tienen mas frecuencias principales pues son mas grandes los valores de la magnitud de la transformada."

datcuad1=np.copy(transfcuad)
where3=np.where(np.abs(transfcuad)<20)
datcuad1[where3]=0

where4=np.where(np.abs(transfcub)<20)
datcub1=np.copy(transfcub)
datcub1[where4]=0


datcuad2=np.copy(transfcuad)
where3=np.where(np.abs(transfcuad)<10)
datcuad2[where3]=0

where4=np.where(np.abs(transfcub)<10)
datcub2=np.copy(transfcub)
datcub2[where4]=0


plt.subplot(221)
plt.plot(freqcub, np.abs(datcub1),label="Interpolacion cubica corte 1000")
plt.legend(loc=0)
plt.xlim(-0.25,0.25)
plt.subplot(222)
plt.plot(freqcuad, np.abs(datcuad1),label="Interpolacion cuadratica corte 1000")
plt.legend(loc=0)
plt.xlim(-0.25,0.25)
plt.subplot(223)
plt.plot(freqcub,np.abs(datcub2),label="Datos originales corte 500" )


plt.legend(loc=0)
plt.xlim(-0.25,0.25)
plt.subplot(224)
plt.plot(freqcuad,np.abs(datcuad2),label="Datos originales corte 500" )


plt.legend(loc=0)
plt.xlim(-0.25,0.25)
plt.savefig("CordobaRafael_2Filtros.pdf")
plt.clf()
