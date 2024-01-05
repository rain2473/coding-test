from collections import deque

N = int(input())

queue = deque([])
answer = deque([])
show = 0

for _ in range(N):
    tmp = input()
    
    try:
        order, x = map(int, tmp.split(' '))
    except:
        order = int(tmp)
        
    if order == 1:
        queue.appendleft(x)
        continue
    elif order == 2:
        queue.append(x)
        continue
    elif order == 3:
        try:
            show = queue.popleft()
        except:
            show = -1
    elif order == 4:
        try:
            show = queue.pop()
        except:
            show = -1
    elif order == 5:
        show = len(queue)
    elif order == 6:
        show = 1 * (len(queue) == 0)
    elif order == 7:
        try:
            show = queue[0]
        except:
            show = -1
    elif order == 8:
        try:
            show = queue[-1]
        except:
            show = -1
    answer.append(show)
    
while answer:
    print(answer.popleft())