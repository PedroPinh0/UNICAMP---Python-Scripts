# -*- coding: utf-8 -*-
import numpy as np

###################################################################
#--Essa função calcula o gradiente de um campo escalar------------#
#--f(x,y), discreto com pontos equidistantes. As entradas são-----#
#--um grid com informações dos valores de f(x,y) para cada--------#
#--ponto e o espaçamento entre eles. O código faz as derivadas----#
#--direcionais levando em conta a posição do ponto no array.------#
#--Pontos nas bordas são calculados por "forward differences"-----#
#--ou "backwards differences" enquanto que os centrais são--------#
#--calculados por "central differences".--------------------------#
###################################################################

def Grad(file, h):
    f = np.asanyarray(file)
    Nx, Ny = np.shape(f)[0], np.shape(f)[1]
    
    dx = np.zeros([Nx,Ny], float)
    dy = dx.copy()
    
    # Cálculo de df/dy
    for i in range(Nx):
        for j in range(Ny):
            # 'Forward diff.' para pontos na borda superior
            if i == 0:
                dy[i,j] = (f[i+1,j] - f[i,j])/h            
            # 'Backward diff.' para pontos na borda inferior
            if i == Nx - 1:
                dy[i,j] = (f[i,j] - f[i-1,j])/h             
            # 'Central diff.' para pontos interiores
            else:
                dy[i,j] = (f[i+1,j] - f[i-1,j])/(2*h)            
    
    # Cálculo de df/dy
    for i in range(Nx):
        for j in range(Ny):
            # 'Forward diff.' para pontos na borda esquerda
            if j == 0:
                dx[i,j] = (f[i,j+1] - f[i,j])/h
            # 'Backward diff.' para pontos na borda direita
            if j == Ny - 1:
                dx[i,j] = (f[i,j] - f[i,j-1])/h
            # 'Central diff.' para pontos interiores
            else:
                dx[i,j] = (f[i,j+1] - f[i,j-1])/(2*h)            
            
    return dx,dy
    
H     = np.loadtxt('altitude.txt')
h     = 3000
dx,dy = Grad(H, h)

print(dx, '\n', dy)