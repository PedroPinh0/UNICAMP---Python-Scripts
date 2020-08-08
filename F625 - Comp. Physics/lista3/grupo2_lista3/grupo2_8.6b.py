# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

###########################################################
#--Função contendo a EDO para o oscilador anaharmônico----#
#--reduzida para um sistema de 2 EDO's de primeira ordem.-#
###########################################################
def F(p):
    x  = p[0]
    dx = p[1]
    F1 = dx
    F2 = -x**3
    return np.array([F1,F2], float)

# Resolução por meio de RK4
def EDO_solve(F,T,p):
    x  = []
    dx = []

    for t in T:
        x.append(p[0])
        dx.append(p[1])

        k1 = h*F(p)
        k2 = h*F(p + k1/2)
        k3 = h*F(p + k2/2)
        k4 = h*F(p + k3)
        p += (k1 + 2*k2 + 2*k3 + k4)/6
    
    return np.array([x,dx], float)

# Condições iniciais
p0 = [1,0] # Amplitude 1
p1 = [2,0] # Amplitude 2

# Intervalo de tempo
a = 0
b = 50    
N = 1000
h = (b-a)/N
T = np.arange(a,b,h)

# Gráfico da evolução temporal do oscilador
plt.figure(figsize = (15,5))
plt.plot(T, EDO_solve(F,T,p0)[0], '.-k', label = 'x0 = 1', markersize = 3)
plt.plot(T, EDO_solve(F,T,p1)[0], '.-r', label = 'x0 = 2', markersize = 3)
plt.xlabel('t [s]', size = 14)
plt.ylabel('x [m]', size = 14)
plt.grid(alpha = 0.2)
plt.legend(loc = 'lower left')
plt.show()

# Gráfico do espaço de fase do oscilador 
fig, ax = plt.subplots()
plt.plot(EDO_solve(F,T,p0)[0], EDO_solve(F,T,p0)[1], '-k', label = 'x0 = 1', markersize = 3)
plt.plot(EDO_solve(F,T,p1)[0], EDO_solve(F,T,p1)[1], '-r', label = 'x0 = 2', markersize = 3)
plt.xlabel('x [m]', size = 14)
plt.ylabel('dx/dt [m/s]', size = 14)
plt.legend(loc = 'lower left')
ax.set_xlim(-3,3)
ax.set_aspect(aspect = 'equal')
plt.show()