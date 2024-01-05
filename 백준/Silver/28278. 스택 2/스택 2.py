from collections import deque

N = int(input())

stack = []
answer = deque([])
show = 0

for _ in range(N):
    tmp = input()
    
    try:
        order, x = map(int, tmp.split(' '))
    except:
        order = int(tmp)
        
    if order == 1:
        stack.append(x)
        continue
    elif order == 2:
        try:
            show = stack.pop()
        except:
            show = -1
    elif order == 3:
        show = len(stack)
    elif order == 4:
        show = 1 * (len(stack) == 0)
    elif order == 5:
        try:
            show = stack[-1]
        except:
            show = -1
    answer.append(show)
    
while answer:
    print(answer.popleft())