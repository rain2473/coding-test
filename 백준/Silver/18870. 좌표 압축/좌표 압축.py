n = int(input())
ls = list(map(int,input().split(" ")))
idx = sorted(list(set(ls)))
d = {idx[i] : i for i in range(len(idx))}
for i in ls:
    print(d[i], end = ' ')