from collections import deque
def solution(storey):
    answer, queue, result = 0, deque(), []
    queue.append([storey, answer])
    while queue:
        storey, answer = queue.popleft()
        a, b = storey % 10, 10 - (storey % 10)
        storey = storey // 10
        if storey == 0:
            result.append(a + answer)
            result.append(b + 1 + answer)
        else:
            queue.append([storey, a + answer])
            queue.append([storey + 1, b + answer])
    return min(result)