# -*- coding: utf-8-sig -*-
import numpy as np

##################################################
#--Programa que recebe o número de atomos (N)----#
#--na aresta de um cubo com N^3 átomos de NaCL---#
#--e calcula a constante de Madelung-------------#
#--aproximada para esse número de átomos.--------#
##################################################

# Recebendo o número de átomos
L  = int(input("Número de átomos em uma aresta do cubo: "))
M = 0

# Varrendo para cada átomo nas posições (i,j,k) 
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            # Cálculo da distância até o átomo central
            d = np.sqrt(i**2 + j**2 + k**2)
            # Ignorando o átomo central
            if (i == j == k == 0):
                continue
            
            M_parc = 1/d
            # Alternando entre íons negativos e positivos
            if (i + j + k)%2 == 1:
                M_parc *= -1
            # Adicionando contribuição individual ao valor final
            M += M_parc
            
print('Constante de Madelung para o cristal de NaCl: %.3f' %abs(M))