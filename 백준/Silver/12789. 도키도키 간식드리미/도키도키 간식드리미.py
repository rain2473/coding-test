from collections import deque

n = int(input())
ans = "Nice"

get = 0
stay = [n + 1]

line = deque(list(map(int, input().split(" "))))

while line:
    if stay[-1] == get + 1:
        get = stay.pop()
        continue
        
    now = line.popleft()
    
    if now == get + 1:
        get = now
   
    elif now < stay[-1]:
        stay.append(now)
        
    else:
        ans = "Sad"
        break
print(ans)