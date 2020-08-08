# -*- coding: utf-8 -*-
import numpy as np

# Parâmetros
m     = 9.109383701e-31  #[Kg]
hbar  = 1.054516817e-34  #[J*s]
e     = 1.602176634e-19  #[C]
V0    = 50*e             #[J]
a     = 1.0e-11          #[m]
N     = 1000
h     = 20*a/N

X = np.arange(-10*a,10*a,h)

# Potencial restaurador do oscilador harmônico
def V(x):
    return V0*(x/a)**2

#######################################################
#--Função contendo a esquação de Schrodinger reduzida-#
#---a um sistema de duas EDOs de primeira ordem-------#
#######################################################
def F(r,x,E):
    psi = r[0]
    phi = r[1]
    Fpsi = phi
    Fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return np.array([Fpsi,Fphi],float)

# Solução da EDO por RK4 tendo a energia como parâmetro
def Schrd_Solve(F,r0,E):
    r   = r0.copy()
    Psi = np.array([],float)
    for x in X:
        Psi = np.append(Psi, r[0])
        k1 = h*F(r,x,E)
        k2 = h*F(r+0.5*k1,x+0.5*h,E)
        k3 = h*F(r+0.5*k2,x+0.5*h,E)
        k4 = h*F(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6
    return Psi 

#Condições iniciais
#err: Incerteza no cálculo da energia
r0 = np.array([0.0,1.0])
err = e/1e4

# Array onde será armazenado as energias de cada estado
E_array = np.array([], float)

# Chute inicial para o intervalo da energia do Est. Fund.
E1 = 0
E2 = e

# Calculo das energias pelo método da secante
psi2 = Schrd_Solve(F,r0,E1)[-1]
for k in range(3):
    while abs(E2 - E1) > err:
        psi1, psi2 = psi2, Schrd_Solve(F,r0,E2)[-1]
        E1,E2 = E2, E2 - psi2*(E2 - E1)/(psi2 - psi1)
    
    E_array = np.append(E_array,E2)
    E1 = E2*1.5
    E2 = E1 + e
    
print("Energia do estado fundamental, em eV: %f" %(E_array[0]/e))
print("Energia do primeiro estado excitado, em eV: %f" %(E_array[1]/e))
print("Energia do segundo estado excitado, em eV: %f" %(E_array[2]/e))