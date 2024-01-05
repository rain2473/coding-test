from collections import deque

N = int(input())

queue = deque([])
answer = deque([])
show = 0

for _ in range(N):
    tmp = input()
    
    try:
        order, x = map(str, tmp.split(' '))
    except:
        order = str(tmp)
        
    if order == 'push':
        queue.append(x)
        continue
    elif order == 'pop':
        try:
            show = queue.popleft()
        except:
            show = -1
    elif order == 'size':
        show = len(queue)
    elif order == 'empty':
        show = 1 * (len(queue) == 0)
    elif order == 'front':
        try:
            show = queue[0]
        except:
            show = -1
    elif order == 'back':
        try:
            show = queue[-1]
        except:
            show = -1
    answer.append(show)
    
while answer:
    print(answer.popleft())