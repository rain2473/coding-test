import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while True:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        b = heapq.heappop(scoville)
        new = a + 2 * b
        heapq.heappush(scoville,new)
        count += 1
        if len(scoville) == 1 and scoville[0] < K:
            count = -1
            break
    return count