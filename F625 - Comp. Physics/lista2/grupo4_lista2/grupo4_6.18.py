# -*- coding: cp1252 -*-
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab

def f(x):
    return x**3/(np.exp(x) - 1)

############################################################
#--Esse c�digo calcula a efici�ncia (percentual da---------#
#--intensidade emitida na faixa do v�sivel) para uma-------#
#--l�mpada (aproximada para um corpo negro). A efici�ncia--#
#--� calculada para uma temperatura T do corpo.------------#
############################################################

def Eff(T):
    # k: Constante de Boltzmann
    # c: Velocidade da luz
    # h: Constante de Planck
    # lamb_i: Limites da faixa de radia��o v�sivel
    
    k      = 1.38064852e-23  # [m^2 kg s^-2 k^-1]
    c      = 299792458       # [m/s]
    h      = 6.62607015e-34  # [m^2 kg/s]
    lamb_1 = 390e-9          # [m]
    lamb_2 = 750e-9          # [m]
    
    a = (h*c)/(k*T*lamb_2)
    b = (h*c)/(k*T*lamb_1)
    
    # Integração Gaussiana
    N     = 100
    xp,wp = gaussxwab(N, a, b)
    I = 0
    for k in range(N):
        I += wp[k]*f(xp[k])
        
    return 15*I/np.pi**4

T   = np.linspace(300, 10000, 100)
eff = np.array([Eff(T) for T in T])

#####################################################################
#--Tendo o perfil da efici�ncia pela temperatura podemos------------#
#--calcular a temperatura de maior efici�ncia pelo m�todo-----------#
#--de busca da raz�o aurea. A fun��o necessita do array-------------#
#--onde ser� feita a busca, pontos in�ciais e uma acur�cia limite.--#
#####################################################################
def gld_srch(f, p0, acc):
    x0, x3 = p0[0], p0[1]
    phi    = (1 + np.sqrt(5))/2
    d      = (x3 - x0)/phi
    
    x1 = x0 + d
    x2 = x3 - d
    
    while (x3 - x0) > acc:
        if f(x1) > f(x2):
            x0 = x2
            x2 = x1
            x1 = x0 + (x3 - x0)/phi
            
        else:
            x3 = x1
            x1 = x2
            x2 = x3 - (x3 - x0)/phi
    
    return (x3 + x0)/2

# A temperatura de m�xima efici�ncia � calcula com precis�o de 1K
Max_T = gld_srch(Eff, [6e3,8e3], 1)                
print("A temperatura de maior efici�ncia �: %d K" %Max_T)

plt.plot(T/1000, eff, '-k')
plt.grid(alpha = 0.5)
plt.xlabel('T[k]/1000', size = 14)
plt.ylabel('Efici�ncia', size = 14)
plt.axvline(x = Max_T/1000, linestyle = '--', color = 'r', ymax = 0.96)
plt.text(7, 0.35, "6928 K", fontsize = 12)
plt.show()