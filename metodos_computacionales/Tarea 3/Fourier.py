import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
from scipy.interpolate import interp1d

signal=np.genfromtxt("signal.dat",delimiter =",")
incompletos=np.genfromtxt("incompletos.dat",delimiter =",")


plt.plot(signal[:,0],signal[:,1],label= "Datos signal")
plt.legend(loc=0)
plt.title("Signal.dat")
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
freq=fft.fftfreq(len(X),d=(signal[1,0]-signal[0,0]))
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
plt.title("Transformada de Fourier discreta")
plt.savefig("CordobaRafael_TF.pdf")
##Frecuancias principaples

where =np.where(np.abs(freq)<1000)
freq1=np.copy(freq)
transrec=np.copy(X)

where2 =np.where(np.abs(freq)>1000)
transrec[where2]=0+0j
plt.clf()
plt.plot(freq,np.abs(transrec),label="Transformada filtro pasa bajos corte 1000 Hz")
plt.legend(loc=0)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Norma de la Transformada")
plt.title("Transformada Fourier filtrada")
#plt.show()
plt.clf()
plt.plot(t,np.real(fft.ifft(transrec)),label="Signal con filtro pasa bajos corte 1000 Hz")
plt.legend(loc=0)
plt.xlabel("Tiempo")
plt.ylabel("Signal")
plt.title("Signal Filtrada")
plt.savefig("CordobaRafael_filtrada.pdf")




print "Las frecuencias principales son:" ,freq[where]


print "No se puede aplicar la Transformada a los datos incompletos por que no estan igualemnte espaciados."
cuadratica = interp1d(incompletos[:,0],incompletos[:,1],kind ='quadratic')
cubica = interp1d(incompletos[:,0],incompletos[:,1], kind='cubic')
t=np.linspace(np.amin(incompletos[:,0]),np.amax(incompletos[:,0]),512)
datcub=cubica(t)
datcuad=cuadratica(t)


transfcub=fft1(datcub)
freqcub=fft.fftfreq(len(transfcub),d=t[1]-t[0])
transfcuad=fft1(datcuad)
freqcuad=fft.fftfreq(len(transfcuad),d=t[1]-t[0])

plt.clf()
plt.subplot(131)
plt.plot(freqcub, np.abs(transfcub),label="Interp cub")
plt.legend(loc=0)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Norma ")
plt.xlim(-1000,1000)
plt.ylim(0,650)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)
plt.subplot(132)
plt.plot(freqcuad, np.abs(transfcuad),label="Interp cuad")
plt.legend(loc=0)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Norma ")
plt.xlim(-1000,1000)

plt.ylim(0,650)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)
plt.subplot(133)
plt.plot(freq,np.abs(X),label="Originales" )
plt.legend(loc=0)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Norma ")
plt.xlim(-1000,1000)
plt.subplots_adjust(wspace=0.5)

plt.ylim(0,650)
plt.savefig("CordobaRafael_TF_interpola.pdf")
plt.clf()




print "Se ve que las graficas interpoladas tienen mas frecuencias principales pues son mas grandes los valores de la magnitud de la transformada, ademas tienen mayor magnitud las componentes con frecuencia mayor a 1000 Hz."

datcuad1=np.copy(transfcuad)
where3=np.where(np.abs(freqcuad)>1000)
datcuad1[where3]=0

where4=np.where(np.abs(freqcub)>1000)
datcub1=np.copy(transfcub)
datcub1[where4]=0


datcuad2=np.copy(transfcuad)
where3=np.where(np.abs(freqcuad)>500)
datcuad2[where3]=0

where4=np.where(np.abs(freqcub)>500)
datcub2=np.copy(transfcub)
datcub2[where4]=0


transrec500=np.copy(X)
where2 =np.where(np.abs(freq)>500)
transrec500[where2]=0+0j

plt.subplot(211)
plt.plot(t, np.real(fft.ifft(datcub1)),label="Cubica corte 1000 Hz")
plt.plot(signal[:,0],np.real(fft.ifft(transrec)),label="Datos corte 1000 Hz" )
plt.plot(t, np.real(fft.ifft(datcuad1)),label="Cuadratica corte 1000 Hz")
plt.legend(loc=0)
plt.title("Filtro pasa bajos corte 1000 Hz")





plt.subplot(212)
plt.plot(signal[:,0],np.real(fft.ifft(transrec500)),label="Datos corte 500 Hz" )
plt.plot(t,np.real(fft.ifft(datcub2)),label="Cubica corte 500 Hz" )
plt.plot(t,np.real(fft.ifft(datcuad2)),label="Cuadratica corte 500 Hz" )

plt.title("Filtro pasa bajos corte 500 Hz")

plt.legend(loc=0)
plt.subplots_adjust(wspace=0.5,hspace=0.5)

plt.savefig("CordobaRafael_2Filtros.pdf")
plt.clf()
