# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#########################################################################
#--Programa que calcula a intensidade de irradiação solar sobre um------#
#--terreno dado ângulo de incidência. Em especial, com esse programa----#
#--podemos simular uma imagem 3D de uma varredura da superficie---------#
#--do sílicio por meio de um Microscópio de Varredura por Tunelamento.--#
#########################################################################

def Grad(file, h):
    f = np.asanyarray(file)
    Nx, Ny = np.shape(f)[0], np.shape(f)[1]
    
    dx = np.zeros([Nx,Ny], float)
    dy = dx.copy()
    
    for i in range(Nx):
        for j in range(Ny):
            if i == 0:
                dy[i,j] = (f[i+1,j] - f[i,j])/h            
            if i == Nx - 1:
                dy[i,j] = (f[i,j] - f[i-1,j])/h             
            else:
                dy[i,j] = (f[i+1,j] - f[i-1,j])/(2*h)            
    
    for i in range(Nx):
        for j in range(Ny):
            if j == 0:
                dx[i,j] = (f[i,j+1] - f[i,j])/h
            if j == Ny - 1:
                dx[i,j] = (f[i,j] - f[i,j-1])/h
            else:
                dx[i,j] = (f[i,j+1] - f[i,j-1])/(2*h)            
           
    return dx,dy

Si_stm = np.loadtxt('stm.txt')

h     = 2.5
theta = (45/180)*np.pi
dx,dy = Grad(Si_stm, h)

I = (np.cos(theta)*dx + np.sin(theta)*dy)/(dx**2 + dy**2 + 1)**0.5

plt.imshow(I, cmap = 'gray')
plt.show()