n = int(input( "Digite um número inteiro paar fatoração em primos:"))

prime = 2
prime_list = []

while prime < n:
    number = 2
    is_prime = True
    while number < prime and is_prime:
        if number != 1:
            if prime % number == 0:
                is_prime = False
            else:
                number+=1
    if is_prime:
            prime_list.append(prime)
    prime+=1
    
    
print(prime_list)
    

factor = []
division = n
while(division > 1):
    for n in prime_list:
        if(division % n == 0):
            division = division/n
            factor.append(n)
            break

factor.append(1)
print("os fatores primos são:",factor)

print(result)

primes = [i]
print = i
primes.append(i)

