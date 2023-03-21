from collections import deque
import heapq
def solution(n, k, enemy):
    answer = 0
    cost = 0
    heap = []
    enemy = deque(enemy)
    while enemy:
        e = enemy.popleft()
        cost += e
        heapq.heappush(heap, -e)
        if cost <= n:
            pass
        elif k > 0:
            cost += heapq.heappop(heap)
            k -= 1
        else:
            break
        answer +=1
    return answer