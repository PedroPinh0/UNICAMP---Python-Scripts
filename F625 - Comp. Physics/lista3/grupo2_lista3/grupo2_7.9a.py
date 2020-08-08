import numpy as np
import matplotlib.pyplot as plt

# Leitura do arquivo com dados
pic_blur = np.loadtxt('blur.txt')

plt.figure(figsize = (5,5))
plt.imshow(pic_blur, cmap = 'gray')
plt.show()