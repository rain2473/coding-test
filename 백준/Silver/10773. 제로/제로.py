N,stack = int(input()), []
for i in range(N):
    tmp = int(input())
    if tmp != 0:
        stack.append(tmp)
    else:
        stack.pop()
print(sum(stack))