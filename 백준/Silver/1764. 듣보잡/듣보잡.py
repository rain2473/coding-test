import heapq
import sys
# input = sys.stdin.readline

names = dict([])
answer = []

M, N = map(int,input().split(' '))

for i in range(M + N):
    name = input()
    
    try:
        names[name] += 1
        answer.append(name)
    except:
        names[name] = 0
        
    answer = sorted(answer)
print(len(answer))
for name in answer:
    print(name)