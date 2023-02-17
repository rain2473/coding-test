from collections import deque
def solution(x, y, n):
    answer, queue = -1, deque([(y,0)])
    while queue:
        (y, tmp) = queue.popleft()
        if y == x:
            answer = tmp
            break
        tmp += 1
        if y % 3 == 0 and y // 3 >= x:
            queue.append((y // 3, tmp))
        if y % 2 == 0 and y // 2 >= x:
            queue.append((y // 2, tmp))
        if y > x:
            queue.append((y - n, tmp))
    return answer