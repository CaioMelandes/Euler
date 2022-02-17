# The sum of the squares of the first ten natural numbers is, 385
# The square of the sum of the first ten natural numbers is, 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.

numeros = [i for i in range(1,101)]
quadrado_da_soma = sum(numeros) ** 2
soma_dos_quadrados = 0

for i in numeros:
    soma_dos_quadrados += i ** 2
    
print(quadrado_da_soma - soma_dos_quadrados)