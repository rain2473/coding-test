from collections import deque
def ex(a,b,c,d):
    tmp = a.popleft()
    b.append(tmp)
    c, d = c - tmp, d + tmp
    return c, d

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    answer = 0
    while sum1 != sum2:
        answer += 1
        if sum1 > sum2:
            sum1, sum2 = ex(queue1, queue2, sum1, sum2)
        else:
            sum2, sum1 = ex(queue2, queue1, sum2, sum1)
        if answer > (len(queue1)+len(queue2))*2:
            answer = -1
            break
    return answer