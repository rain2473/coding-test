a, b, c = map(int,input().split(" "))
tmp = (a % b)
for i in range(c-1):
    tmp *= 10
    tmp %= b
tmp = tmp *10//b
print(tmp)