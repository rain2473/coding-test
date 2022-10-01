N = int(input())
tmp = []
for n in range(N):
    a,b = input().split(' ')
    a = int(a)
    temp = (a,n,b)
    tmp.append(temp)
    
tmp = sorted(tmp)
for i,j,k in tmp:
    print(f'{i} {k}')