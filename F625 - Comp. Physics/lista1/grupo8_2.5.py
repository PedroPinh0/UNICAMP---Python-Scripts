# -*- coding: utf-8-sig -*-
import numpy as np

#--Sequência de programas que calculam---#
#--respectivamente a probabilidade de----#
#--transmissão e reflexão de um----------#
#--elétron com energia "E_electron" ao---#
#--encontrar uma barreira de potencial---#
#--de valor "E_step"---------------------#

def transmission(E_step, E_electron):
    if E_electron <= E_step:
        print("ERRO: ENERGIA DO ELÉTRON DEVE SER MAIOR QUE POTENCIAL")
    m    = 9.11e-31                                 #[kg]
    hbar = 6.58e-16                                 #[eV*s]
    k1   = np.sqrt(2*m*E_electron)/hbar
    k2   = np.sqrt(2*m*(E_electron - E_step))/hbar
    T    = (4*k1*k2)/((k1 + k2)**2)
    return T

def reflection(E_step, E_electron):
    if E_electron <= E_step:
        print("ERRO: ENERGIA DO ELÉTRON DEVE SER MAIOR QUE POTENCIAL")
    m    = 9.11e-31                                 #[kg]
    hbar = 6.58e-16                                 #[eV*s]
    k1   = np.sqrt(2*m*E_electron)/hbar
    k2   = np.sqrt(2*m*(E_electron - E_step))/hbar
    R    = ((k1 - k2)/(k1 + k2))**2
    return R


#Recebendo dados do usuário
E_electron = float(input("Energia do elétron (em eV): "))
E_step     = float(input("Energia do potencial (em eV): "))

#Calculando as probabilidades
T, R = transmission(E_step, E_electron), reflection(E_step, E_electron)

print("As probabilidades são T = %.2f e R = %.2f" %(T,R))