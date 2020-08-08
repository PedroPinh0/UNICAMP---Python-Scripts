# -*- coding: utf-8 -*-
# p0 : Chute inicial
# a,b: Parametros do modelo
p0 = [1,1]
a  = 1
b  = 2

# Inicializando soluções
x,y  = p0[0], p0[1]

# Número de iterações
N    = 100
for i in range(N):
    # Atualizando soluções
    x = y*(a - x**2)
    y = b/(a + x**2)
    
    print(x,y)