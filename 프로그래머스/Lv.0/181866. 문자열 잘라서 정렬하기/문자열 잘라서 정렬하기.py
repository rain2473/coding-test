from collections import deque
def solution(myString):
    answer = deque(sorted(myString.split('x')))
    while True:
        if answer[0] == '':
            answer.popleft()
        else:
            break
    return list(answer)