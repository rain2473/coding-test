N = int(input())

if N < 100:
    print(N)
elif N >99 and N <1000:
    ans = 99
    for i in range(100,N+1):
        a = i //100
        b = (i % 100) // 10
        c = i %10
        if 2*b == (a+c):
            ans += 1
    print(ans)
elif N == 1000:
    print(144)