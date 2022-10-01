def decimal(x):
    tmp =[]
    for i in range(1, x+1):
        if x % i ==0:
            tmp.append(i)
    if len(tmp) == 2:
        return x
    else:
        return None
    
N = int(input())
temp = input().split(' ')
cnt = []
for n in range(N):
    temp[n] = int(temp[n])
    cnt.append(decimal(temp[n]))
temp1 = []
for c in cnt:
    if c != None:
        temp1.append(c)
cnt = len(temp1)
print(cnt)