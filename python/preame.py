from math import sqrt

def isPrime(n):
    for i in range(2,round(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

for n in range(2,101):
    print(n,"isPrime:",isPrime(n))