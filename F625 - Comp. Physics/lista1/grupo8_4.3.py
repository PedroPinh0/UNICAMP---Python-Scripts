# -*- coding: utf-8-sig -*-
# Definindo a função que calcula f(x) = x(x-1) 
def func(x):
    return x*(x - 1)

################################################
#--Definfindo a função que calcula a derivada--#
#--por meio do metodo de divisão infinitesimal-#
#--ela recebe como argumentos uma função-------#
#--pré-definida, o ponto onde se calcular a----#
#--derivada e o intervalo delta----------------#
################################################

def derivative(f, a, d):
    deriv = (func(a + d) - func(a))/(d)
    return deriv

print("A derivada de f(x) = x(x-1) em x = 2 é: %.5f" %derivative(func, 1, 1e-2))