


def calculer_interet(n,interet,temps):
    return n*((1+interet)**temps)

# print(calculer_interet(1,0.01,2000))

def u(n):
    if type(n) is not int or n < 0:
        raise TypeError("n doit être un entier plus grand ou égale à 0")
    return 3/(2**n)

n = 0
while u(n) > 10**(-3):
    n += 1
    
# print(n-1,u(n-1))

from random import randint

# print([randint(1,6) for _ in range(6)])

def sommeDeList(L:list) -> float:
    somme = 0
    for v in L:
        somme += v
    return somme

def listeSigne(L:list) -> list:
    nouvelle_L = []
    for v in L:
        if v == 0:
            nouvelle_L.append(v)
        else:
            nouvelle_L.append(int(v/abs(v)))
    return nouvelle_L

print(listeSigne([6584,-654,684,0,-1,59,00]))