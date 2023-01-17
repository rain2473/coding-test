import heapq
def solution(operations):
    maxh, minh, visited = [], [], [False] * len(operations)
    for i,order in enumerate(operations):
        o, n = order.split(" ")
        n = int(n)
        if o == "I":
            heapq.heappush(maxh,(-n,i))
            heapq.heappush(minh,(n,i))
            visited[i] = True
        elif n == 1:
            while maxh and visited[maxh[0][1]] == False:
                heapq.heappop(maxh)
            if maxh:
                visited[maxh[0][1]] = False
                heapq.heappop(maxh)
        else:
            while minh and visited[minh[0][1]] == False:
                heapq.heappop(minh)
            if minh:
                visited[minh[0][1]] = False
                heapq.heappop(minh)
    if True in visited:
        while maxh and visited[maxh[0][1]] == False:
            heapq.heappop(maxh)
        while minh and visited[minh[0][1]] == False:
            heapq.heappop(minh)
        return ([-maxh[0][0], minh[0][0]])
    else:
        return [0,0]