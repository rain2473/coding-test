from sys import stdin
N = int(stdin.readline())
ans = 1
cnt = 0
for i in range(1,N+1):
    ans *= i
while True:
    if ans % 10 ==0:
        cnt +=1
        ans = ans//10
    else:
        break
print(cnt)