from collections import deque

N = int(input())
answer = deque([])

for i in range(N):
    string = input()
    answer.append(string[0] + string[-1])
    
while answer:
    print(answer.popleft())