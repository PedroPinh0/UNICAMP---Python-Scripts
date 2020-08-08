# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Função contendo o sistema de equações de Lorenz
def F(p0):
    sig = 10
    r   = 28
    b   = 8/3
    x,y,z = p0[0], p0[1], p0[2]
    
    Dx = sig*(y - x)
    Dy = x*(r - z) - y
    Dz = x*y - b*z
    
    return np.array([Dx,Dy,Dz], float)

# Espaçamento dos pontos
N  = 10000.0
h  = 50/N

# Array com o intervalo de tempo
T = np.arange(0,50,h)

# Inicialização das soluções
x = np.array([])
y = np.array([])
z = np.array([])

# Condições iniciais
p0 = np.array([0, 1, 0], float)

# Resolução da EDO por meio de RK4
for t in T:
    x = np.append(x, p0[0])
    y = np.append(y, p0[1])
    z = np.append(z, p0[2])
    
    k1 = h*F(p0)
    k2 = h*F(p0 + k1/2)
    k3 = h*F(p0 + k2/2)
    k4 = h*F(p0 + k3)
    p0 += (k1 + 2*k2 + 2*k3 + k4)/6

# Apresentação da solução
plt.figure(figsize = (15,5))
plt.plot(T, y, '-k')
plt.xlabel('T [u.a]', size = 14)
plt.ylabel('Y [u.a]', size = 14)
plt.show()

plt.figure(figsize = (15,5))
plt.plot(x, z, '-k')
plt.xlabel('X [u.a]', size = 14)
plt.ylabel('Z [u.a]', size = 14)
plt.show()