# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Leitura do arquivo contendo os dados
dow_data = np.loadtxt('dow.txt')

# Figura e gráfico da curva
plt.figure(figsize = (15,5))
plt.plot(dow_data, '-k')
plt.xlabel("# dia", size = 14)
plt.ylabel("[US$]", size = 14)
plt.grid(alpha = 0.5)
plt.show()