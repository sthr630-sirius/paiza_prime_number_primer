n = int(input())
max_score = 6000000
is_prime = [True]*(max_score+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, max_score+1):
    if is_prime[i]:
        for j in range(i*2, max_score+1, i):
            is_prime[j] = False
#for i in range(1, n+1):
#    print(i, is_prime[i])
#print(is_prime)

for _ in range(n):
    score = int(input())
    if is_prime[score]:
        print("pass")
    else:
        print("failure")