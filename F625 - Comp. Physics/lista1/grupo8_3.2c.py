# -*- coding: utf-8-sig -*-
import numpy as np
import matplotlib.pyplot as plt

#Criação do array com valores Teta e r
a = np.linspace(0, 12*np.pi, 1000)
r = np.exp(np.cos(a)) - 2*np.cos(4*a) + (np.sin(a/12))**5

#Conversão para cartesianas
x = r*np.cos(a)
y = r*np.sin(a)

#Gráfico
plt.plot(x, y, '.k-', markersize = 2)
plt.grid(alpha = 0.5)
#plt.savefig('ex_3.2c.jpg', dpi = 300)
plt.show()