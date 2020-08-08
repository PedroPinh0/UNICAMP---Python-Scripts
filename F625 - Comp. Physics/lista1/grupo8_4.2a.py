# -*- coding: utf-8 -*-
###########################################
#--Função que recebe os coeficientes da---#
#--equação ax^2 + bx + c = 0 e calcula----#
#--as rai­zes do polinómio por meio da-----#
#--equação x = (-b +- sqrt(b^2 - 4ac))/2a-#
###########################################

def quad(a, b, c):
    sol = [(-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a)]
    return sol

# Recebendo os coeficientes e atribuindo as variaveis
a,b,c = map(float, input("Coeficientes (a,b,c): ").split())
# Calculando soluções
sol = quad(a, b, c)

print('\nAs soluções sÃo: {:.12f} e {:.12f}'.format(sol[0], sol[1]))