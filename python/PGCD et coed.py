def PGCD(n1,n2):
    a = n1
    b = n2
    qs = []
    r = 1
    while r > 0:
        r = a % b
        q = a // b
        qs.append(q)
        print(f'{a} = {b} * {q} + {r}')
        a = b
        b = r
    qs = qs[:-1]
    
    u0 = 1
    v0 = -qs[0]
  
    if len(qs) > 2:
        v1 = qs[0]*qs[1] + 1
        u1 = -qs[1]
        for i in range(2,len(qs)):
            uh = u0 - qs[i]*u1
            vh = v0 - qs[i]*v1
            u0 = u1
            v0 = v1
            u1 = uh
            v1 = vh 
        return f'PGCD : {a}, {n1} * {u1} + {n2} * {v1} = {n1*u1+n2*v1}.'
    elif len(qs) == 1:
        return f'PGCD : {a}, {n1} * {u0} + {n2} * {v0} = {n1*u0+n2*v0}.'
    elif len(qs) == 2:
        v1 = qs[0]*qs[1] + 1
        u1 = -qs[1]
        return f'PGCD : {a}, {n1} * {u1} + {n2} * {v1} = {n1*u1+n2*v1}.'
        
print(PGCD(5484657,674536))