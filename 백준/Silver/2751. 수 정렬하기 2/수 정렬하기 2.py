import sys
T = int(sys.stdin.readline())
tmp =[]
for t in range(T):
    tmp.append(int(sys.stdin.readline()))
for t in sorted(tmp):
    print(t)