from collections import deque
def solution(n, computers):
    graph = {i:[] for i in range(n)}
    for i, com in enumerate(computers):
        for j in range(len(com)):
            if com[j] == 1 and i!=j:
                graph[i] += [j]
    queue, connected, answer, start = deque(), [0]*(n), 0, 0
    while connected != [1]*(n):
        queue.append(start)
        connected[start] = 1
        while queue:
            vertex = queue.popleft()
            for i in graph[vertex]:
                if connected[i] == 0:
                    queue.append(i)
                    connected[i] = 1
        answer += 1
        for i,c in enumerate(connected):
            if c != 1:
                start = i
                break
    return answer