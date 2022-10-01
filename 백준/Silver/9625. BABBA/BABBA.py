tmp  = [1,0]
n = int(input())
for i in range(n):
    a = tmp[0]
    b = tmp[1]
    tmp[0] = b
    tmp[1] = a+b
print(tmp[0], tmp[1])