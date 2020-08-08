# -*- coding: utf-8 -*-
import numpy as np
from math import factorial as fact

##################################################
#--Programa que calcula a m-ésima derivada de----#
#--uma função f(z) em z=0 utilizando a Integral--#
#--de Cauchy no plano complexo. A integral é-----#
#--aproximada pelo método de trapézios onde o----#
#--caminho da integral é o circulo unitário------#
#--centrado na origem.---------------------------#
##################################################

# Função a ser derivada
def f(z):
    return np.exp(2*z)

def deriv_f(m):
    N = 10000
    i = complex(0,1)
    
    Sum = 0
    for k in range(N):
        Sum += f(np.exp(i*2*np.pi*k/N))*np.exp(-i*2*np.pi*k*m/N)
        
    return fact(m)*Sum/N

# As 21 primeiras derivadas de f(z = 0) são calculadas 
m = np.array(range(1,21))
deriv = np.array([deriv_f(m) for m in m])

# Os elementos de 'deriv' são essencialmente complexo, vamos imprimir
# seus modulos arredondados em 2 casas decimais
print([round(abs(deriv[i]), 2) for i in range(len(deriv))])