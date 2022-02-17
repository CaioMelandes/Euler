# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

# Função que verifica se o número é primo
def primo(numero):
    raiz = int(sqrt(numero))
    
    for i in range(2,raiz+1):
        if numero % i == 0:
            return False
    
    return True

maior_fator = 0
const = 600851475143

for i in range(3,const+1,2):
    # Condição de parada
    if const == 1:
        break
    
    # Caso seja primo tentará a divisão 
    elif primo(i):
        if const % i == 0:
            const /= i
            if i > maior_fator:
                maior_fator = i

# Mostra o maior fator
print(maior_fator)