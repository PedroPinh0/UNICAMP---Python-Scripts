# -*- coding: utf-8 -*-
from vpython import sphere, vector, canvas

# O número de átomos totais é (2N+1)^3 cujos raios são iguais a R
L = 2
R = 0.5

# Inicializando a figura
scene = canvas(title='Sodium Cloride Lattice')
# Varrendo cada posição (i,j,k) e colocando um átomo
for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L + 1):
            # Alternando entre átomos de sódio e de cloro
            if (i+j+k)%2 == 0:
                sphere(pos = vector(i,j,k), radius = R, color = vector(1,1,0))
            else:
                sphere(pos = vector(i,j,k), radius = R)