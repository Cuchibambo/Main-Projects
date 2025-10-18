import math
import matplotlib as plt
# Diviseurs d'un nombre
# n = (5^4)-1
# for i in range(n):
#     if n % (i+1) == 0:
#         print(i+1)

# Nombres parfaits
# for j in range(131070,131072):
#     L = []
#     sum = 0
#     for i in range(1,j+1):
#         if j % (i) == 0:
#             L.append(i)
#     L.remove(j)
#     for i in range(len(L)):
#         sum += L[i]
#     if sum == j:
#         print(j)

# test pour trouver a et b
# def findab(q,r,sum,rangeup):
#     for b in range(r+1,rangeup+1):
#         test = q*b+r
#         if test + b == sum:
#             a = test
#             return (a,b)
    
# print(findab(4,64,434,76,65))

# u = 1
# for i in range(99999):
#     u = (1/3)*(u)+i-2
#     print(i+1,u)

# def deriv_kxn(k,n):
#     return k*n,'x',(n-1)

# print(deriv_kxn(1,0.5))

def u(d,k,x,n):
    n_factorial = math.factorial(n)
    n_d_factorial = math.factorial(n-d)
    k = (k*n_factorial)/(n_d_factorial)
    n = n-d
    ans = x**n
    ans = ans*k
    return ans

def fullsum(d,x):
    for i in range(2**(d-1)):
        sum = 0
        sum += u(d-i,)

print(fullsum(2,0))