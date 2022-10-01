import math
n = int(input())
tmp = math.floor(math.log2(n))
ans = 2*(n - 2 ** tmp)
if ans == 0:
    print(n)
else:
    print(ans)