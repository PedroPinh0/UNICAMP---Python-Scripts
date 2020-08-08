# -*- coding: utf-8-sig -*-
import numpy as np
import matplotlib.pyplot as plt

#Criação do array com valores Teta
a = np.linspace(0, 2*np.pi, 100)

#Conversão para cartesianas
x = 2*np.cos(a) + np.cos(2*a)
y = 2*np.sin(a) - np.sin(2*a)

#Gráfico
plt.plot(x, y, '.k-')
plt.ylim(-3,3)
plt.grid(alpha = 0.5)
#plt.savefig('ex_3.2a.jpg', dpi = 300)
plt.show()