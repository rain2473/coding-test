from collections import deque
def solution(targets):
    answer = 0
    targets = deque(sorted(targets, key = lambda x : x[1]))
    tmp = targets.popleft()
    shot = tmp[1] - 0.5
    while targets:
        tmp = targets.popleft()
        if shot < tmp[0]:
            answer += 1
            shot = tmp[1] - 0.5
    return answer + (shot > tmp[0])