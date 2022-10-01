from sys import stdin
n= int(stdin.readline())
deque = []
for i in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == 'pop_front':
        if len(deque) != 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)
    elif 'push_front' == cmd[0]:
        deque = [cmd[1]]+deque
    elif 'push_back' == cmd[0]:
        deque.append(cmd[1])