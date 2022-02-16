# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Função que verifica se o número é um palindromo
def palindromo(numero):
    numero = str(numero)
    
    # Verifica se a string é igual a ela revertida
    if numero == numero[::-1]:
        return True
    
    return False
  
maior_palindromo = 0

# Inicia a contagem pelo maior valor de três digitos 999
for i in range(999,100,-1):
    j = 999
    
    # Verfica se é maior para evitar repetições
    while j >= i:
        if palindromo(i*j) and (i*j) > maior_palindromo:
            maior_palindromo = i * j
            break
        else:
            j -= 1

print(maior_palindromo)