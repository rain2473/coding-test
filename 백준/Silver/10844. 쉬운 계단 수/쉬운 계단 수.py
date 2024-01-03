N = int(input())

tmp = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    tmp[1][i] = 1

for j in range(2, N + 1):
    for i in range(10):
        if i == 0:
            tmp[j][i] = tmp[j - 1][i + 1]
        elif i == 9:
            tmp[j][i] = tmp[j - 1][i - 1]
        else:
            tmp[j][i] = tmp[j - 1][i - 1] + tmp[j - 1][i + 1]

answer = sum(tmp[N]) % 1000000000
print(answer)
