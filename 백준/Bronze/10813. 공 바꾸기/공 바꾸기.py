N, M = map(int,input().split(' '))

bucket = [str(i + 1) for i in range(N)]

for m in range(M):
    a, b = map(int,input().split(' '))
    tmp = bucket[a - 1]
    bucket[a - 1] = bucket[b - 1]
    bucket[b - 1] = tmp
               
print(" ".join(bucket))