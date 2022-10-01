n = int(input())
for i in range(n):
    a,b = map(int,input().split(" "))
    tmp = 1
    if a>= b//2:
        for j in range(a+1,b+1):
            tmp = tmp * j / (j-a)
    else:
        for k in range(1,a+1):
            tmp = tmp * (b-a+k) / k
    tmp = int(tmp)
    print(tmp)