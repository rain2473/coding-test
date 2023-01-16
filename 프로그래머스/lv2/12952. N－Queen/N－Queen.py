def solution(n):
    def check(visited, new):
        for i in range(len(visited)):
            if new == visited[i] or (len(visited)-i) == abs(visited[i]-new):
                return False
        return True
    
    def dfs(n, visited):
        if len(visited) == n:
            return 1
        count = 0
        for i in range(n):
            if check(visited, i):
                count += dfs(n, visited+[i])
        return count
        
    return dfs(n, [])