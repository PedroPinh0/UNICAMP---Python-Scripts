# -*- coding: utf-8-sig -*-
#########################################################
#--Função que corrige o problema de cálculo-------------#
#--de ponto flutuante ao achar a raiz-------------------#
#--maior de ax^2+bx+c por meio da equação---------------#
#--(-b - (b**2 - 4*a*c)**0.5)/(2*a) e a raiz------------#
#--menor por meio de (2*c)/(-b - (b**2 - 4*a*c)**0.5).--#
#########################################################
def quad_opt(a, b, c):
    sol = [(2*c)/(-b - (b**2 - 4*a*c)**0.5), (-b - (b**2 - 4*a*c)**0.5)/(2*a)]
    return sol

# Recebendo dados do usuário
a,b,c = map(float, input('Coeficientes: ').split())

# Calculando as raizes
sol_opt = quad_opt(a, b, c)

print('\nAs soluções são: {:.12E} e {:.12E}'.format(sol_opt[0], sol_opt[1]))