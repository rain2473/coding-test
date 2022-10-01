import sys
n = int(sys.stdin.readline())

tmp =[1 for _ in range(n+2)]
tmp[0]=0
for i in range(3,n+2):
    tmp[i] = tmp[i-1]%15746 + tmp[i-2]%15746
print(tmp[-1]%15746)