N = int(input())
tmp = sorted(map(int,input().split(' ')))
M = int(input())
temp = list(map(int,input().split(' ')))
ans = {}

for i in tmp:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=1
        
for i in temp:
    if i in ans:
        print(ans[i], end = ' ')
    else:
        print(0, end = ' ')