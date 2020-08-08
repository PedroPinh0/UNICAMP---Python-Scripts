# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

##################################################
#--Esta função calcula os coeficientes da--------#
#--transformada de Fourier de uma amostragem-----#
#--discreta e entrega uma amostragem com grau----#
#--'reduzido' ao remover frequências, ou melhor,-#
#--anulando parte dos coeficientes definidos-----#
#--pelo usuário.---------------------------------#
##################################################

def FT_interp(f,perc):
    # Calculo da transformada de fourier
    f_FT = np.fft.rfft(f)
    
    # Aniquilação do coeficientes não desejados
    N = len(f_FT)
    f_FT[int(N*perc):] = 0
    
    # Calcul    o da transformada inversa do novo array reduzido
    f_inFT = np.fft.irfft(f_FT)
    return f_inFT

# Leitura dos dados
dow_data = np.loadtxt('dow.txt')

# Gráfico dos dados originais
plt.figure(figsize = (15,5))
plt.plot(dow_data, '-k', label = 'Dados reais')

# Gráfico dos dados com 10% dos coeficientes
plt.plot(FT_interp(dow_data,0.1), '-r', label = "FT Interpolation 10%")

# Grafico com 2% dos coeficientes
plt.plot(FT_interp(dow_data,0.02), '--b', label = "FT Interpolation 2%")

plt.xlabel("# dia", size = 14)
plt.ylabel("Pontos", size = 14)
plt.grid(alpha = 0.5)
plt.legend(loc = 'best')
plt.show()