from sys import stdin
N = int(stdin.readline())
D = [1,0,3,0]
if N > 3:
    for n in range(4, N+1):
        if n % 2 == 1:
            D.append(0)
        else:
            D.append(4 * D[n-2] - D[n-4])
print(D[N])