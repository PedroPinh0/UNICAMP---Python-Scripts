# -*- coding: utf-8 -*-
from vpython import sphere, vector, canvas

###################################################
#--Programa que desenha uma estrutura cristalina--#
#--de tipo FCC - face-centered cubic. A lógica----#
#--se basea no fato que a FCC pode ser vista------#
#--como uma CS onde os átomos de posição impar----#
#--estão em falta. Posição ímpar sendo aquela-----#
#--onde (i+j+k) é ímpar.--------------------------#
###################################################

# Número de átomos na aresta é (L+1)/2 cujos raios são R
L = 7
R = 0.7

#Inicializando a figura
scene = canvas(title='Fcc Lattice')
#Varrendo para cada posição (i,j,k)
for i in range(L):
    for j in range(L):
        for k in range(L):
            # Se a posição for par adiciona um átomo, c.c pula a posição
            if (i+j+k)%2 == 0:
                sphere(pos = vector(i,j,k), radius = R)
            else:
                continue