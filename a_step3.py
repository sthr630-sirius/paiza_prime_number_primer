import math

n = int(input())
is_prime = True
n_sqrt = int(math.sqrt(n))
if n == 1:
    is_prime = False

for i in range(2, n_sqrt+1):
    if n%i == 0:
        is_prime = False

if is_prime:
    print("YES")
else:
    print("NO")