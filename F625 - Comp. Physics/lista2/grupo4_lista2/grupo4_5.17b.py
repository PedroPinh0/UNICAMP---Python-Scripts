# -*- coding: utf-8 -*-
import numpy as np
from gaussxw import gaussxwab

##############################################
#--Função que calcula a função Gamma para----#
#--um deteminado valor de 'a'. Para evitar---#
#--erro de precisão, a troca de variavel-----#
#--z = x/(x + a - 1) foi feita, alterando o--#
#--intervalo de integração de [0, \inf] para-#
#--[0, 1].-----------------------------------#
##############################################

def gamma(a):
    c = a - 1
    
    # Integrando da função Gamma na nova variável z
    def f(c,z):
        return c* np.exp(c*(np.log(c*z/(1-z)))) * np.exp(-(c*z)/(1-z))/(1 - z)**2
    
    # Integração feita por método de Quadratura Gaussiana
    N = 50
    zp, wp = gaussxwab(N, 0, 1)
    
    I = 0.0
    for k in range(len(zp)):
        I+= wp[k]*f(c,zp[k])
    
    # O valor de Gamma(a) é entregue arredondado
    return round(I,4)

# Testando a função para calcular um valor conhecido e alguns fatoriais
a = [3/2, 3, 6, 10]
print([gamma(a_i) for a_i in a])