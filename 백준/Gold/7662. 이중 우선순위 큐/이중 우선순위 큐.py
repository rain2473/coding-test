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
        return [-maxh[0][0], minh[0][0]]
    else:
        return "EMPTY"

N = int(input())
for n in range(N):
    T = int(input())
    operations = []
    for t in range(T):
        operations.append(input())
    answer = solution(operations)
    if answer == "EMPTY":
        print(answer)
    else:
        print(answer[0], answer[1])