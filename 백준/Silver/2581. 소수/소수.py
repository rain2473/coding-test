def decimal(x):
    tmp =[]
    for i in range(1, x+1):
        if x % i ==0:
            tmp.append(i)
    if len(tmp) == 2:
        return x
    else:
        return None
    
M = int(input())
N = int(input())
temp = []
temp1 = []
for n in range(M, N+1):
    temp.append(decimal(n))
for t in temp:
    if t != None:
        temp1.append(t)

if sum(temp1) != 0:
    print(f'{sum(temp1)}\n{sorted(temp1)[0]}')
else:
    print(-1)