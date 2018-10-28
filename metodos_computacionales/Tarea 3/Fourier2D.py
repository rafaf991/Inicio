import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fftpack import ifftn,fftn
from PIL import Image
from collections import Counter

from scipy import fftpack, ndimage,misc
import matplotlib.pyplot as plt

image = ndimage.imread('Arboles.png')
scipy.misc.imsave('outfile1.jpg', image)

fft2 = fftpack.fft2(image)
FreqCompRows = np.fft.fftfreq(fft2.shape[0],d=2)
FreqCompCols = np.fft.fftfreq(fft2.shape[1],d=2)
print FreqCompCols
print FreqCompRows
plt.plot(FreqCompCols,fft2)
plt.plot(FreqCompCols,fft2)
plt.xlim(-0.5,0.5)
plt.show()
plt.clf()
plt.imshow(np.log10(abs(fft2)))
plt.colorbar()
plt.show()



filtrada=np.copy(fft2)
#ruido 20-60 10-1000
where1=np.where((abs(filtrada)>1000000) & (abs(filtrada)<2000000 ))

filtrada[where1]=0
plt.clf()
plt.imshow(np.log10(abs(filtrada)))
plt.colorbar()
imfiltrada=ifftn(filtrada)
imfiltrada=np.array(imfiltrada)
imfiltrada=Image.fromarray(imfiltrada.astype('uint8'))
imfiltrada.show()
plt.show()
scipy.misc.imsave('outfile.jpg', imfiltrada)
