p = int(input())
a = 2
r = a%p
is_prime = True
if p%a == 0:
    is_prime = False
else:
    for _ in range(2, p):
       r = (r*a)%p
    if r != 1:
        is_prime = False

if is_prime:
    print("YES")
else:
    print("NO")