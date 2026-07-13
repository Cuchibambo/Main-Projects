from random import randint
N = 61
n = 10
random_numbers = [randint(1,N) for _ in range(n)]
# random_numbers = [21, 22, 103, 237, 248, 255, 261, 276, 279, 318]
average = sum(random_numbers)/n
predicted_N = (average*2)-1
print(f'N : {N}, n : {n}')
print(f'numbers : {random_numbers}')
print(f'average : {average}')
print(f'expected average : {(N+1)/2}')
print(f'predicted N : {round(predicted_N)}')
print(f'error : {abs(N-predicted_N)}')