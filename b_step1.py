n = int(input())
is_prime = [True]*(n+1)
is_prime[0] = False
is_prime[1] = False
prime_number = []
for i in range(2, n+1):
    if is_prime[i]:
        for j in range(i*2, n+1, i):
            is_prime[j] = False

for i in range(2, n+1):
    if is_prime[i]:
        prime_number.append(i)

for i in prime_number:
    while n >= i:
        if n%i == 0:
            print(i)
            n = n // i
        else:
            break