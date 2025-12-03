import math
import matplotlib.pyplot as plt
import numpy as np
import random

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
    
# print(findab(4,64,434,76))

# Suite recurence Template
# u = 1
# for i in range(99999):
#     u = (1/3)*(u)+i-2
#     print(i+1,u)

# Derivees polynomiales
# manual = True
# x_min, x_max = -10, 10
# y_min, y_max = -10, 10

# axx = np.linspace(x_min,x_max,5*(abs(x_min)+abs(x_max))+1)
# # d = 2
# k=10*random.random()
# n=random.randint(1,5)
# k1=10*random.random()
# n1=random.randint(1,5)
# k2=10*random.random()
# n2=random.randint(1,5)

# def f(x):
#     u=k*(x**n)+k1*(x**n1)+k2*(x**n2)
#     # v=5*(x**2)
#     return u

# # def f1(x):
# #     u=k*n*(x**(n-1))
# #     return u

# # def f2(x):
# #     u=k*n*(n-1)*(x**(n-2))
# #     return u

# def u(d,k,x,n):
#     # handle cases where n and n-d are non-negative integers; if derivative order is larger than power, return zero
#     n_minus_d = n - d
#     # if the resulting power is negative, the (integer) derivative is zero for polynomial terms
#     if n_minus_d < 0:
#         return np.zeros_like(x)
#     # use integer factorials (cast to int for safety)
#     n_int = int(n)
#     n_minus_d_int = int(n_minus_d)
#     n_factorial = math.factorial(n_int)
#     n_d_factorial = math.factorial(n_minus_d_int)
#     coeff = (k * n_factorial) / (n_d_factorial)
#     ans = (x ** n_minus_d) * coeff
#     return ans

# # def fullsum(d,x):
# #     sum = 0
# #     for i in range(2**(d-1)):
# #         sum += u(d-i,2,x,4)*u(i,5,x,2)+u(i,2,x,4)*u(d-i,5,x,2)
# #     return sum

# axy0 = f(axx)
# axy1 = u(97,k,axx,100)+u(97,k1,axx,99)+u(97,k2,axx,98)
# axy2 = u(2,k,axx,n)+u(2,k1,axx,n1)+u(2,k2,axx,n2)
# plt.plot(axx,axy0,'g-')
# plt.plot(axx,axy1,'r-')
# plt.plot(axx,axy2,'b-')

# print("Function: {}x^{} + {}x^{} + {}x^{}".format(round(k,2),n,round(k1,2),n1,round(k2,2),n2))

# if manual:
#     plt.xlim(x_min, x_max)
#     plt.ylim(y_min, y_max)
#     # set ticks (adjust count as needed)
#     # plt.xticks(np.linspace(x_min, x_max, 11))
#     # plt.yticks(np.linspace(y_min, y_max, 11))
# else:
#     plt.autoscale()
# plt.grid(True)
# plt.show()

def dot1(u,v):
    return (u[0]*v[0])+(u[1]*v[1])

def dot2(magu,magv):
    return (((magu+magv)**2)-(magu**2)-(magv**2))/2

def getMag(u):
    return math.sqrt((u[0]**2)+(u[1]**2))

u = (1,5)
v = (-1,3)

print(dot1(u,v),dot2(getMag(u),getMag(v)))