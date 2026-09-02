seed = 308657924
temp1 = seed ^ (seed >> 13)
temp2 = temp1 ^ (temp1 << 17)
result = temp2 ^ (temp2 >> 5)

print(f"seed: {seed}\ntemp1: {temp1}\ntemp2: {temp2}\nresult: {result}")