import math

n = int(input())
is_prime = [True]*(n+1)
is_prime[0] = False
is_prime[1] = False

prime_list = []

for i in range(2, int(math.sqrt(n))+1):
    if is_prime[i]:
        for j in range(i*2, n+1, i):
            is_prime[j] = False

for i in range(n+1):
    if is_prime[i]:
        prime_list.append(i)

ans = 1

for i in prime_list:
    counter = 0
    while n%i == 0:
        n = n//i
        counter += 1
    ans = ans * (counter+1)

print(ans)