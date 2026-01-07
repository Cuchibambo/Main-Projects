import numpy as np
import matplotlib.pyplot as plt

def CalculerLamda(i:list[float,float],a:list[float,float],D:list[float,float]):

    def Alea(L:list):
        return np.random.normal(L[0],L[1])

    d = []
    Iteration = 10000
    for _ in range(Iteration):
        Alea_Lambda = Alea(i)*Alea(a)/Alea(D)
        d.append(Alea_Lambda*1e9)

    Lambda = np.mean(d)
    u_Lambda = np.std(d, ddof=1)
    return Lambda, u_Lambda

i = (,)
a = (0.0002,)
D = (2,)

Lambda, u_Lambda = CalculerLamda(i,a,D)
print('\nLongeure d\'onde Lambda =', Lambda,' nm')
print('Incertitide-Type : u(Lambda) =', u_Lambda,' nm')

