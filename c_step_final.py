import math
def check_prime(m):
    is_prime = True
    for i in range(2, int(math.sqrt(m))+1):
        if m%i == 0:
            is_prime = False
            print(m+2)
            break
    return is_prime

n = 10**8

check_sqrt_num = []
for i in range(3, int(math.sqrt(n))+1, 2):
    check_sqrt_num.append(i**2)

is_ans = True

for sqrt_num in check_sqrt_num:
    is_ans = check_prime(sqrt_num-2)

if is_ans:
    print("paiza's conjecture is correct.")