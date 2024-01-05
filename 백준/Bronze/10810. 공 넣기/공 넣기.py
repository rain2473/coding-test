N, M = map(int,input().split(' '))

bucket = ['0'] * N

for m in range(M):
    a, b, c = map(int,input().split(' '))
    for i in range(a - 1, b):
        bucket[i] = str(c)
               
print(" ".join(bucket))