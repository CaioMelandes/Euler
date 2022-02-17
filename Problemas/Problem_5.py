# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Começa por 20 por ser o maior divisor
dividendo = 20

while True:
    for i in range(1,21):
        
        # Testa se a divisão atual tem resto, para não fazer testes desnecesários
        if dividendo % i != 0:
            dividendo += 1
            break
    
    # Como 20 é o último divisor, somente se i tiver o valor dele é que todos os outros funcionaram
    if i == 20:
        print(dividendo)
        break