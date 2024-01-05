N, M = map(int,input().split(' '))

bucket = [str(i + 1) for i in range(N)]

for m in range(M):
    a, b = map(int,input().split(' '))
    front = bucket[0 : a - 1]
    reverse_ = list(reversed(bucket[a - 1 : b]))
    back = bucket[b : ]
    bucket = front + reverse_ + back
               
print(" ".join(bucket))