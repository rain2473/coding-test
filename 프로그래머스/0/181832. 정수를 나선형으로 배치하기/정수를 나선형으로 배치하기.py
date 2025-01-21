from collections import deque
def solution(n):
    answer = calc(n)
    return answer

def calc(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1,2], [4,3]]
    else:
        result = deque([])
        num = 2 * n -1
        for i, row in enumerate(calc(n-1)):
            tmp = deque([])
            for e in row:
                tmp.appendleft(e + num)
            tmp.append(num - i)
            result.appendleft(list(tmp))
        result.appendleft([i + 1 for i in range(n)])
        return list(result)