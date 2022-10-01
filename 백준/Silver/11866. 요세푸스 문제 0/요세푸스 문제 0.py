n, k = map(int, input().split())
tmp = [i for i in range(1,n+1)]
comp = []
cnt = 0
while tmp:
    cnt += k-1
    if cnt >=len(tmp):
        cnt %= len(tmp)
    comp.append(str(tmp.pop(cnt)))
    
print('<',', '.join(comp),'>',sep='')