from numpy.random import random
from numpy import exp, pi, cos, sqrt, log
import matplotlib.pyplot as plt

# Aqui nós definimos uma função que retorna o valor da função que desejamos
# minimizar.
def f(x):
    return(cos(x) + cos(sqrt(2) * x) + cos(sqrt(3) * x))

# Aqui definimos constantes como a "temperatura" máxima e mínima,a constante de
# resfriamento e o valor inicial de x.
Tmax = 1
Tmin = 1e-5
tau = 1e5
x0 = 15

# Aqui calculamos o valor da função em x0, iniciamos a "temperatura" como a 
# máxima, x como x0 e criamos o array que vai receber os valores x.
fx = f(x0)
t = 0
T = Tmax
x = x0
grafx = []

# Aqui damos inicio ao loop principal.
while T>Tmin:

    # Acrescimo do tempo.
    t += 1
    
    # Resfriamento.
    T = Tmax * exp(-t / tau)
    
    # Aqui salvamos os valores antigos de x e f(x).
    antx = x
    antfx = fx
    
    # Aqui acrescentamos um valor aleatório ao valor de x e calculamos
    # o novo valor para f(x).
    theta = 2 * pi * random()
    r = sqrt(-2 * 1 ** 2 * log(1 - random()))
    x += r * cos(theta)
    fx = f(x)
    
    
    if x<0 or x>50:
        x = antx
        fx = antfx
        continue
     
    # Aqui calculamos a diferença entre o valor novo e antigo de fx.
    dfx = fx - antfx
    
    # Aqui vemos se o novo valor sera aceito ou não.
    if random()>=exp(-dfx/T):
        x = antx
        fx = antfx
    grafx.append(x)

# Aqui printamos o valor de x e f(x).
print('x =',x,'fx =',fx)

# Aqui printamos o gráfico de x por tempo.
plt.figure(dpi = 300)
plt.plot(grafx, '.k', markersize = 1)
plt.ylabel('x', size = 14)
plt.xlabel('Tempo', size = 14)
plt.savefig('ex10_10_img2')
plt.show()