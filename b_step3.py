import math

n = int(input())
max_num = 100000

digit = [100000]*int(math.sqrt(max_num)+1)
digit[0] = 0
digit[1] = 0

for i in range(0, n):
    m = int(input())
    for j in range(2, int(math.sqrt(max_num)+1)):
        counter = 0
        while m%j == 0:
            counter += 1
            m = m//j
        digit[j] = min(digit[j], counter)
    #print(digit)

ans = 1

for i, v in enumerate(digit):
    ans = ans * i**v

print(ans)