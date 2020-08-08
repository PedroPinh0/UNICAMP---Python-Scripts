# -*- coding: utf-8 -*-
import numpy as np

a = 10         #[eV]
L = 5e-10      #[m]

# Esta função calcula os elementos H_mn da matrix do Hamiltoniano 
def H_mn(m,n,a,L):
    h_bar = 1.0546e-34 #[Js]
    M     = 9.1094e-31 #[kg]
    q     = 1.6022e-19 #[C]
    
    # A carga do elétron é utilizada para converter eV em J
    if m == n:
        Hmn = (a*q)/2 + (h_bar*n*np.pi/L)**2/(2*M)
        return Hmn/q
    
    if m!=n and (m+n)%2 != 0:
        Hmn = (-8*a*q*m*n)/(np.pi*(m**2 - n**2))**2
        return Hmn/q 
    
    else: 
        return 0
    
m,n = list(map(int, input("Digite m e n separados por espaço: ").split()))
print(H_mn(m,n,a,L))