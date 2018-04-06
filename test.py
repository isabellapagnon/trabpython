"""
Spyder Editor

This is a temporary script file.
"""

print(1)

numero = input("Digite um numero inteiro para ser fatorado:")
numero = int(numero)
#8print(type(numero))
i = [2,3,5,7,11,13,17,19,23,27,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
result = []
div = numero



while(div > 1):
    
    for number in i:
        print(div%number, div, number)
        if (div % number == 0):
            div = div/number
            result.append(number)
            break
        

print(result)

primes = [i]
print = i
primes.append(i)

