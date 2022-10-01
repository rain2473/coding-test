N = int(input())
tmp = []
for n in range(N):
    tmp.append(input())
    
temp = list(set(tmp))

ans = []

for i in range(len(temp)):
    ans.append((len(temp[i]),temp[i]))
ans = sorted(ans)
for i,j in ans:
    print(j)