from collections import deque

N = int(input())
queue = deque(enumerate(map(int, input().split(" "))))
answer = []

while queue:
    idx, num = queue.popleft()
    answer.append(str(idx + 1))
    
    if num > 0:
        queue.rotate(-num + 1)
    elif num < 0:
        queue.rotate(-num)
    
print(" ".join(answer))