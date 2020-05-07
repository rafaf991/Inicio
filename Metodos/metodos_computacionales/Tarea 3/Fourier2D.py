import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fftpack import ifftn,fftn
from scipy import fftpack, ndimage,misc
import matplotlib.pyplot as plt


image = ndimage.imread('Arboles.png')

fft2 = fftpack.fft2(image)
FreqCompRows = np.fft.fftfreq(fft2.shape[0],d=2)
FreqCompCols = np.fft.fftfreq(fft2.shape[1],d=2)

plt.plot(FreqCompCols,np.abs(fft2))
plt.plot(FreqCompCols,np.abs(fft2))
plt.xlim(-0.5,0.5)
#plt.show()


plt.clf()
plt.imshow(10*np.log10(abs(fftpack.fftshift(fft2))),label="Transformada 2D Arboles.")
plt.colorbar()
plt.savefig("CordobaRafael_FT2D.pdf")



filtrada=np.copy(fft2)
#Se ve en la figura de FFtvs freq que el ruido esta en magnitud >1000000 y menor a 2000000
where1=np.where((np.abs(filtrada)>1000000) & (np.abs(filtrada)<2000000 ))

filtrada[where1]=1

filtradashift=np.copy(fftpack.fftshift(filtrada))
from matplotlib.colors import LogNorm
plt.clf()
plt.imshow(abs(filtradashift),norm=LogNorm())
plt.colorbar()
plt.savefig("CordobaRafael_FT2D_Filtrada.pdf")


imfiltrada=ifftn(filtrada)
imfiltrada=np.array(imfiltrada)
misc.imsave("CordobaRafael_Imagen_filtrada.pdf",imfiltrada.real)
