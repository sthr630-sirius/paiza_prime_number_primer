n = int(input())
is_prime = [True]*(n+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, n+1):
    if is_prime[i]:
        k = 2
        while i*k <= n:
            is_prime[i*k] = False
            k += 1
if is_prime[n]:
    print("YES")
else:
    print("NO")