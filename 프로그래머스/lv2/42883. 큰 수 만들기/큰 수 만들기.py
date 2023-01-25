from collections import deque
def solution(number, k):
    answer, number = [], deque(list(number))
    while k != 0 and number:
        tmp = number.popleft()
        if not answer:
            answer.append(tmp)
            continue
        elif answer[-1] > tmp:
            answer.append(tmp)
            continue
        else:
            while answer[-1] < tmp:
                temp = answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
            answer.append(tmp)
    answer = "".join(answer+list(number))
    if k != 0:
        answer = answer[:-k]
    return answer