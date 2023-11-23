import math
n = int(input())
is_prime = [True]*(n+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(math.sqrt(n)+1)):
    if is_prime:
        for j in range(i*2, n+1, i):
            is_prime[j] = False

ans_list = [0, 0]
ans_product = 0

for i in range(n//2+1):
    if is_prime[i]:
        prime = i
        if is_prime[n-prime]:
            if ans_product < prime*(n-prime):
                ans_product = prime * (n-prime)
                ans_list[0] = prime
                ans_list[1] = n-prime
print(ans_list[0])
print(ans_list[1])