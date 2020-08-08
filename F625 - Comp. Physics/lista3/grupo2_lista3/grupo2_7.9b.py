# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Leitura dos dados com a imagem borrada
pic_blur = np.loadtxt('blur.txt')

# N:   Dimensão da imagem
# std: Desvio padrão da 'spread fuction'
N   = np.shape(pic_blur)[0]
std = 25

##############################################################
#--Partindo de um intervalo [inicio, fim] esse código--------#
#--gera o que aqui é denominado de intervalo antissimétrico--#
#--composto pela concatenação dos intervalos [meio, fim] e---#
#--[inicio, meio].-------------------------------------------#
##############################################################
x1 = np.arange(0,N/2,1)
x2 = np.arange(-N/2,0,1)

x = np.concatenate((x1,x2))
y = x.copy()

# Criação do meshgrid para calculo da função spread
X,Y    = np.meshgrid(x,y)
spread = np.exp(-((X)**2 + Y**2)/(2*(std**2)))

# Apresentação da função
plt.figure(figsize = (5,5))
plt.imshow(spread, cmap = 'gray')
plt.show()