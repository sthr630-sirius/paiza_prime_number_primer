m1, m2, b1, b2 = map(int, input().split())
for i in range(m2):
    z = m1 * i + b1
    if z%m2 == b2:
        print(z)