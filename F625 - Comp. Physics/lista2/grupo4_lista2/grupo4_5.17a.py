# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

###################################
#--Programa que gráfica a função--#
#--f(x) = x**(a-1)*np.exp(-x)-----#
#--para diferentes valores de a---#
###################################

def f(a,x):
    return x**(a-1)*np.exp(-x)

# a = array com dif. valores de a
# c = array com cores para cada curva

a = [2, 3, 4]
c = ['-r', '-k', '-b']
x = np.linspace(0,5,100)
y = [f(a,x) for a in a]

for i in range(0,3):
    plt.plot(x, y[i], c[i], label = 'a = %d' %a[i])

plt.legend(loc = 'best')
plt.xlabel('x', size = 14)
plt.ylabel('f(x)', size = 14)
plt.grid()
plt.show()