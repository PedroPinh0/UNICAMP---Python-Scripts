# -*- coding: utf-8-sig -*-
import numpy as np

# Número de partições
N   = 100
# Tamanho das partições
h   = 2/N

####################################
#--Array com valores de -1 até 1---#
#--separados por h. Total de N ----#
#--partições. A integral é a soma--#
#--dos retângulos de base h e------#
#--altura y------------------------#
####################################

x   = np.arange(-1, 1, h)
y   = np.sqrt(1 - x**2)

integral  = sum(h*y)
print('A integral é: %.4f'%integral)