T = int(input())
for t in range(T):
    n = int(input())
    if n>3:
        tmp=[0 for _ in range(n+1)]
        tmp[1]=1
        tmp[2]=2
        tmp[3]=4
        for i in range(4,n+1):
            tmp[i]=tmp[i-1]+tmp[i-2]+tmp[i-3]
    else:
        tmp=[0,1,2,4]
    print(tmp[n])