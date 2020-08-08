# -*- coding: utf-8-sig -*-
import numpy as np
import matplotlib.pyplot as plt

######################################
#--Função que calcula o módulo de----#
#--z = z' + c por método iterativo---#
#--apartir de um ponto inicial ------#
#--z = 0. Caso no final o módulo-----#
#--seja maior que 2 então o z é------#
#--considerado fora do conjunto------#
#--de Mandelbrot e a função retorna--#
#--o número de iterações necessárias-#
#--para que z tomasse módulo maior---#
#--2.--------------------------------#
######################################
def mandelbrot(x,y):
    c = complex(x,y)
    z = 0
    for i in range(1,100):
        if abs(z) > 2:
            return np.log(i)
        z = z**2 + c
    return 0

######################################
#--A número de subdivisões do grid---#
#--é de N*N. Cada ponto é separado---#
#--por d. Assim, a extensão do plano-#
#--considerado é de |x|<=2.5 e-------#
#--|y|<=2.5--------------------------#
######################################
N = 1000
d = 0.004

# Inicialização do grid
grid = np.empty([N,N], np.float)

######################################
#--Varredura por todos os pontos do--#
#--grid calculando os valores de-----# 
#--x e y da variavel z = x + iy.-----#
#--O valores de N/2 e 2N/3 servem----#
#--para fazer a translação do--------#
#--conjunto para que o mesmo apareça-#
#--por completo na figura------------#
######################################
for i in range(N):
    y = d*(i - N/2)
    for j in range(N):
        x = d*(j - N/2)
        grid[i,j] = mandelbrot(x,y)

# Inicializando a figura e salvando-a
plt.figure(figsize = (20,20))
plt.imshow(grid,cmap='hot')
#plt.savefig('mandelbrot.jpg', dpi = 300)
plt.show()