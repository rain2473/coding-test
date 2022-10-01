a = int(input())
tmp = [0,0,]

for i in range(2,a+1):
    tmp.append([])
    if i % 3 == 0:
        tmp[i].append(tmp[i//3]+1)
    if i % 2 == 0:
        tmp[i].append(tmp[i//2]+1)
    if i > 1:
        tmp[i].append(tmp[i-1]+1)
    tmp[i] = min(tmp[i])
    
print(tmp[a])