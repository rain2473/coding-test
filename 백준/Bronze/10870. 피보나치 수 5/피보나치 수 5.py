#import sys
#sys.setrecursionlimit(10**7)
#def Fibonacci(n):
#    if n == 1 or n == 2:
#        return 1
#    else:
#        return Fibonacci(n-2) +Fibonacci(n-1)
#answer = Fibonacci(int(input()))
#print(answer)
# 재귀함수로 풀면 오류 생김

n = int(input())
answer = [0]+[1]*(n+1)
for i in range(2,n+1):
    answer[i] = answer[i-1] + answer[i-2]
print(answer[n])