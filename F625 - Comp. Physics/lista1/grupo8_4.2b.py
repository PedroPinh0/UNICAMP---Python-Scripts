# -*- coding: utf-8 -*-
###########################################
#--Função que recebe os coeficientes da---#
#--equação ax^2 + bx + c = 0 e calcula----#
#--as raízes do polinômio por meio da-----#
#--equação x = 2c/(-b -+ sqrt(b^2 - 4ac))-#
###########################################

def quad(a, b, c):
    sol = [(2*c)/(-b - (b**2 - 4*a*c)**0.5), (2*c)/(-b + (b**2 - 4*a*c)**0.5)]
    return sol

# Recebendo os coeficientes e atribuindo às variaveis
a,b,c = map(float, input("Coeficientes (a,b,c): ").split())
# Calculando soluções
sol = quad(a, b, c)

print('\nAs soluções são: {:.12f} e {:.12f}'.format(sol[0], sol[1]))