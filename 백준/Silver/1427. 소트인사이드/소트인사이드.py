from collections import deque
n = deque(sorted(list(map(int,list(input()))),reverse = True))
answer = ""
while n:
    tmp = n.popleft()
    answer += str(tmp)
print(answer)