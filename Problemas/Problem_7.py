# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

from math import sqrt

# Função que verifica se o número é primo
def primo(numero):
    raiz = int(sqrt(numero))
    
    for i in range(2,raiz+1):
        if numero % i == 0:
            return False
    
    return True

lista_primos = [2]
atual = 3

# Testará de 2 em 2 até que a lista tenha 10001 elementos
while len(lista_primos) <= 10000:
    
    if primo(atual):
        lista_primos.append(atual)
    
    atual += 2

print(lista_primos[-1])