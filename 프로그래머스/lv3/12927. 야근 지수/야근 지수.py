import heapq
def minus(n):
    return -1 * n
def solution(n, works):
    works, answer = list(map(minus,works)), 0
    heapq.heapify(works)
    while n != 0:
        tmp = heapq.heappop(works)
        heapq.heappush(works,tmp+1)
        n -= 1
    for i in works:
        if i < 0:
            answer += i**2
    return answer