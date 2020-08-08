# -*- coding: utf-8-sig -*-
import numpy as np

###############################################
#--Um programa que toma como input o período--#
#--de órbita do satélite e calcula sua--------#
#--altura em relação ao solo------------------#
###############################################
def alt_sat(T):
    G = 6.67e-11     #[m^3 kg^-1 s^-2]
    M = 5.97e24      #[kg]
    R = 6.371e6      #[m]
    
    r = ((G*M*T**2)/(4*np.pi**2))**(1/3)
    return r - R

#Recebendo dados do usuário e convertendo para segundos
T_horas = float(input("Período do satélite (em horas): "))
T_sec   = T_horas * 3600

h = alt_sat(T_sec)

print('A orbita é %.4E km acima do solo.' %(h/1000))