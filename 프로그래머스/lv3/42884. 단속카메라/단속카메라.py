from collections import deque
def solution(routes):
    answer, camera = 0, -30001
    routes.sort(key = lambda x: x[1])
    routes = deque(routes)
    while routes:
        route = routes.popleft()
        if route[0] > camera:
            answer += 1
            camera = route[1]
    return answer