from collections import deque
def bfs(start,visitied,graph):
    queue, visitied[start] = deque([start]), True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visitied[i] == False:
                queue.append(i)
                visitied[i] = True
    return visitied.count(True) -1

def solution(n, wires):
    graph, answer = {i+1 : [] for i in range(n)}, n
    for a,b in wires:
        graph[a] += [b]
        graph[b] += [a]
    for start,not_visit in wires:
        visitied = [False]*(n+1)
        visitied[not_visit] = True
        result = bfs(start,visitied,graph)
        answer = min(abs(result - (n-result)), answer)       
    return answer