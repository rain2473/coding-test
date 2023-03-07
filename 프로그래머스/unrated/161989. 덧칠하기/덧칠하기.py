from collections import deque
def solution(n, m, section):
    answer, section = 1, deque(section)
    vertex = section.popleft()
    while section:
        if section[0] >= vertex + m:
            answer += 1
            vertex = section.popleft()
        else:
            section.popleft()
    return answer