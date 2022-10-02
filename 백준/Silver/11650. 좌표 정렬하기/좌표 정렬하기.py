from sys import stdin
T = int(stdin.readline())
ans = []
for t in range(T):
    (a,b) = map(int,stdin.readline().split(' '))
    ans.append((a,b))
for (a, b) in sorted(ans):
    tmp = str(a)+' '+str(b)
    print(tmp)