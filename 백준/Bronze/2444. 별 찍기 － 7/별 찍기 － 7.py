N = int(input())

tmp = []

for i in range(N):
    row = " " * (N - 1 - i) + "*" * (2 * i + 1)
    tmp.append(row)

tmp += list(reversed(tmp[:-1]))
while tmp:
    print(tmp.pop())