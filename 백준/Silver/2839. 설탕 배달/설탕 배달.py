from sys import stdin
array = []
T = int(stdin.readline())
for i in range(T//3+1):
    arr = []
    for j in range(T//5+1):
        arr.append(3*i + 5*j)
    array.append(arr)
tmp = []
for i in range(T//3+1):
    for j in range(T//5+1):
        if T == array[i][j]:
            tmp.append(i+j)
if len(tmp) > 0:
    print(sorted(tmp)[0])
else:
    print(-1)