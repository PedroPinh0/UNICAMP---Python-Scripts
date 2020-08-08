# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#################################################
#--Este programa demonstra o potencial ao redor-#
#--de duas cargas puntiformes (q1 e q2)---------#
#--separadas por uma distancia D.---------------#
#################################################

def Pot(D,q1,q2):
    # qi:     Valor das cargas em Coulomb
    # D:      Distância entre cargas
    # d:      Espaçamento entre pontos
    # l:      Tamanho do plano
    # eps_0:  Constante elétrica do vácuo
    # N:      Escala do Grid [NxN]
    
    d     = 1e-2       #[m]
    L     = 1          #[m]
    eps_0 = 8.8542e-12 #[C^2 N^-1 m^-2]
    N     = int(L/d)
    
    # Um grid é formado para calcular o potencial em cada ponto
    x = y = np.linspace(-L/2, L/2, N)
    X,Y   = np.meshgrid(x,y, sparse = True)
    
    # R1 e R2 são as distâncias do ponto até as cargas
    R1  = ((X + D/2)**2 + Y**2)**0.5 
    R2  = ((X - D/2)**2 + Y**2)**0.5
    
    pot = (q1/R1 + q2/R2)/(4*np.pi*eps_0)
        
    plt.figure()
    P_color = plt.imshow(pot, extent = [-L/2, L/2, -L/2, L/2])
    plt.xlabel('Posição X [m]', size = 14)
    plt.ylabel('Posição Y [m]', size = 14)
    plt.colorbar(P_color)
    plt.show()

# As cargas são espaçadas por 10cm
D = 10e-2   #[m]

#Carga do elétron
q_e = 1.6e-12  #[C]

# Função recebe a informação da distância das
# cargas, além do seus valores em Coulomb
Pot(D, q_e, q_e)
Pot(D, q_e, -q_e)