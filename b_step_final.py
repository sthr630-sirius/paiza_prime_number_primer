import math
n = int(input())
max_num = 100
#digit_list = [0]*int(math.sqrt(max_num)+1)
digit_list = [0]*(max_num+1)
for i in range(0, n):
    m = int(input())
    for j in range(2, int(math.sqrt(max_num)+1)):
    #for j in range(2, max_num+1):
        counter = 0
        while m%j == 0:
            counter += 1
            m = m//j
        digit_list[j] = max(digit_list[j], counter)
    if m != 1:
        digit_list[m] = 1

ans = 1

for i, v in enumerate(digit_list):
    ans = ans * i**v

print(ans)