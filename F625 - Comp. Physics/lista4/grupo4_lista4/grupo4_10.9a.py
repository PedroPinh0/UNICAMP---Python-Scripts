import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

'''Simulação em estilo Metropolis do Modelo de
Ising para a magnetização de um cristal 2D. As
constantes são tomadas em unidades naturais, onde
T = 1, k_b = 1 e J = 1.'''

# Constantes
rounds = int(1e6)   # Número de rodadas
N      = 20         # Dimensão da matriz
J      = 1          # Constante de Interação
T      = 1          # Temperatura
k_b    = 1          # Constante de Boltzmann
b      = 1/(k_b*T)

# Matriz onde será armazenado os spins
S = (2*np.random.randint(0, 2, size = (N**2)) - 1).reshape(N,N)

def Energy(S):
    # Dimensão da matriz de spins
    N = np.shape(S)[0]
    
    # Cálculo da interação entre vizinhos
    E1 = S[0:N-1,:]*S[1:N,:]   # Interação entre vizinhos verticais
    E2 = S[:,0:N-1]*S[:,1:N]   # Interação entre vizinhos horizontais

    # A energia total é a soma de todas as interações de spins vizinhos
    E = np.sum(E1) + np.sum(E2)
    return -J*E

def Spin_Change(S):
    S_copy = S.copy()

    # Escolha aleatória de um spin
    i = randint(N)
    j = randint(N)
    
    # Cálculo da energia antes e depois da mudança
    E_old = Energy(S_copy)
    S_copy[i,j] *= -1
    E_new = Energy(S_copy)
    
    # Verificação para ver se o movimento é ou não aceito
    dE = E_new - E_old
    if dE > 0:
        if random() < np.exp(-b*dE):
            return S_copy
        else:
            S_copy[i,j] *= -1
            return S_copy
    else:
        return S_copy
        
# Array de armazenamento da evolução da magnetização
M_plot = []
M = np.sum(S)

for k in range(rounds):
    S = Spin_Change(S)
    
    M += np.sum(S)
    
    M_plot.append(M/(k + 1))

plt.figure()
plt.plot(M_plot,'.k', markersize = 1)
plt.xlabel('Rodadas', size = 14)
plt.ylabel('Magnetização [u.a]', size = 14)
plt.grid(alpha = 0.5)
plt.show()