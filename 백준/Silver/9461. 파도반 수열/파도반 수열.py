T = int(input())
for t in range(T):
    n = int(input())
    a = [1,1,2,3,4,5,7,9]+[0 for _ in range(n+1)]
    b = [1,1,1,1,2,2,3,4,5,7,9]+[0 for _ in range(n+1)]
    c = [2,3,4,5,7,9]+[0 for _ in range(n+1)]
    for i in range(5,n+1):
        a[i] = c[i-1]
        b[i] = c[i-5]
        c[i] = a[i]+b[i]
    print(b[n])