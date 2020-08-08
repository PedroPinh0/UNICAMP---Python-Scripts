# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#########################################
#--Esse programa retorna a função de----#
#--transmissão (q(u)) de uma grade de---#
#--difração com distância entre fendas--#
#--igual a d.---------------------------#
#########################################

d = 20e-6    #[m]

x = np.linspace(-2*d, 2*d, 500)
q = np.sin(np.pi*x/d)**2

plt.plot(x*1e6, q, "-k")
plt.xlabel('Posição na grade [um]', size = 14)
plt.ylabel('q(u)', size = 14)
plt.grid(alpha = 0.5)
plt.show()