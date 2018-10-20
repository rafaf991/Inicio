import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft


signal=np.genfromtxt("signal.dat",delimiter =",")
incompletos=np.genfromtxt("incompletos.dat",delimiter =",")


plt.plot(signal[:,0],signal[:,1],label= "Datos signal")
plt.legend(loc=0)
plt.savefig("CordobaRafael_signal.pdf")


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
print freq
print freq2
t=np.linspace(0,len(X),len(X))
plt.clf()
plt.plot(t,np.abs(X),label="Transformada implementacion propia")
#plt.plot(t,50+np.abs(fft.fft(signal[:,1])),label="Transformada implementacion np.")
plt.legend(loc=0)
plt.savefig("CordobaRafael_TF.pdf")
#plt.show()
