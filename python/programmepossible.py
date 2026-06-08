def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1
    
verified_numbers = {1}
verified_numbers.add(1)
pending_numbers = set()

for current_number in range(1,99):
    pending_numbers.add(current_number)
    next_number = f(current_number)
    if next_number in verified_numbers:
        for pn in pending_numbers:
            verified_numbers.add(pn)
        pending_numbers.clear()
        print(current_number)
    else:
        