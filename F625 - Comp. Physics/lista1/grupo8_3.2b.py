# -*- coding: utf-8-sig -*-
import numpy as np
import matplotlib.pyplot as plt

#Criação do array com valores Teta e r
a = np.linspace(0, 10*np.pi, 300)
r = a**2

#Conversão para cartesianas
x = r*np.cos(a)
y = r*np.sin(a)

#Gráfico
plt.plot(x, y, '.k-')
plt.grid(alpha = 0.5)
#plt.savefig('ex_3.2b.jpg', dpi = 300)
plt.show()