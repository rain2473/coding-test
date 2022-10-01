N = int(input())
ans=[]
for n in range(N):
    cnt = 0
    tmp = list(input())
    for i in range(1,len(tmp)):
        if tmp[i] == tmp[i-1]:
            tmp[i-1]=''
    tmp1=[]
    for s in tmp:
        if s != '':
            tmp1.append(s)
    tmp1 = len(list(set(tmp1)))
    for t in tmp:
        if t !='':
            cnt +=1
    if cnt==tmp1:
        ans.append(1)
    else:
        ans.append(0)
print(sum(ans))