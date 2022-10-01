n = int(input())
if n>2:
    tmp=[0 for _ in range(n+1)]
    tmp[1]=1
    tmp[2]=2
    for i in range(3,n+1):
        tmp[i]=tmp[i-1]+tmp[i-2]
else:
    tmp=[0,1,2]
print(tmp[n]%10007)