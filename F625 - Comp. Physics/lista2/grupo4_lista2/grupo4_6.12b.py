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
    x = ((b - a*y)/y)**0.5
    y = x/(a + x**2)
    
    print(x,y)