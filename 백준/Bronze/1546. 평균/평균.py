N = int(input())
tmp = input().split(' ')
M = 0
tot = 0
for n in range(N):
    tmp[n] = int(tmp[n])
    tot += tmp[n]
    if tmp[n] > M:
        M = tmp[n]
print((tot/N)/M*100)