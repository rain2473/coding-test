from collections import deque
def solution(operations):
    answer = deque([])
    for order in operations:
        try:
            if order == "D 1":
                answer.pop()
            elif order == "D -1":
                answer.popleft()
            else:
                tmp = int(order[2:])
                answer.append(tmp)
                answer = deque(sorted(answer))
        except:
            continue
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0,0]