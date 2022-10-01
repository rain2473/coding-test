from sys import stdin
n= int(stdin.readline())
stack = []
for i in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    elif 'push' == cmd[0]:
        stack.append(cmd[1])