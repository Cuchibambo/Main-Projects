import math
import matplotlib.pyplot as plt
import numpy as np
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

axx = np.linspace(-10,10,100)
# d = 2
k=2
n=4

def f(x):
    u=k*(x**n)
    # v=5*(x**2)
    return u

def u(d,k,x,n):
    n_factorial = math.factorial(n)
    n_d_factorial = math.factorial(n-d)
    k = (k*n_factorial)/(n_d_factorial)
    n = n-d
    ans = x**n
    ans = ans*k
    return ans

def fullsum(d,x):
    sum = 0
    for i in range(2**(d-1)):
        sum += u(d-i,2,x,4)*u(i,5,x,2)+u(i,2,x,4)*u(d-i,5,x,2)
    return sum

axy0 = f(axx)
axy = u(1,k,axx,n)
axy2 = u(2,k,axx,n)
plt.plot(axx,axy,'r--')
plt.plot(axx,axy2,'b-')
plt.plot(axx,axy0,'g-')
plt.grid(True)
plt.show()