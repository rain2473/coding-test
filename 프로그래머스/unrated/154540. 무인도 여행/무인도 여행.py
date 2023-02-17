from collections import deque
def solution(maps):
    answer, field = [], []
    for line in maps:
        field.append(list(line))
    row, col = len(field[0]), len(field)
    for y in range(col):
        for x in range(row):
            if is_able(y,x,field):
                answer.append(dfs((y,x), field))
    answer = sorted(answer) * (answer != []) + ([-1]) * (answer == [])
    return answer

def dfs(start, field):
    answer = 0
    queue = deque([start])
    while queue:
        (y,x) = queue.pop()
        try:
            answer += int(field[y][x])
        except:
            pass
        field[y][x] = "C"
        for (ny, nx) in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
            if is_able(ny, nx, field):
                queue.append((ny, nx))
    return answer
            
def is_able(y,x,field):
    answer, row, col = False, len(field[0]), len(field)
    if x >= 0 and x < row and y >= 0 and y < col:
        if field[y][x] != "X" and field[y][x] != "C":
            answer =  True
    return answer
