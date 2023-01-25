from collections import deque
def dijkstra(distance, table):
    queue = deque([])
    queue.append([1,0])
    while queue:
        node, cost = queue.popleft()
        for n, c in table[node]:
            if cost+c < distance[n]:
                distance[n] = cost+c
                queue.append([n, cost+c])
    pass

def solution(N, road, K):
    distance = [float("inf")]*(N+1)
    distance[1] = 0
    table = [[] for i in range(N+1)]
    for r in road:
        table[r[0]].append([r[1],r[2]])
        table[r[1]].append([r[0],r[2]])
    dijkstra(distance, table)
    return len([i for i in distance if i <= K])