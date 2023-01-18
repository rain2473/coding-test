from collections import deque
N, M, start = map(int,input().split())
graph, visited_dfs, visited_bfs = {i+1 : [] for i in range(N)}, [False for i in range(N+1)], [False for i in range(N+1)]
for m in range(M):
    a, b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]
for i in range(N):
    graph[i+1].sort()
    
def bfs(graph, visited, start):
    vertex, answer, que = start, [start], deque(graph[start])
    visited[start],visited[0] = True, True
    
    while False in visited and len(que) != 0:
        vertex = que.popleft()
        if visited[vertex] == False:
            que += graph[vertex]
            answer.append(vertex)
            visited[vertex] =True
    return answer

def dfs(graph, visited, start):
    vertex, answer, stack = start, [start], graph[start][::-1]
    visited[start],visited[0] = True, True
    
    while False in visited and len(stack) != 0:
        vertex = stack.pop()
        if visited[vertex] == False:
            stack += graph[vertex][::-1]
            answer.append(vertex)
            visited[vertex] =True
    return answer

dfs = dfs(graph, visited_dfs, start)
bfs = bfs(graph, visited_bfs, start)

for d in dfs:
    print(d, end =" ")
print()    
for b in bfs:
    print(b, end =" ")