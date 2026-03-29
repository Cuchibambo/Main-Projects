nbdejavue = set()
for a in range(3,12+1):
    for b in range(2,8+1):
        for c in range(1,6+1):
            if c < b and b < a: 
                N = (a**3)+2*(b**3)+(c**3)
                if N < 2025:
                    if N in nbdejavue:
                        print(N)
                    else:
                        nbdejavue.add(N)
print(len(nbdejavue))