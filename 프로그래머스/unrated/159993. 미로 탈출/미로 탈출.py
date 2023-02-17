from collections import deque
def solution(maps):
    field1, field2, sle = [], [], {"S" : (), "L" : (), "E" : ()}
    for y,line in enumerate(maps):
        field1.append(list(line))
        field2.append(list(line))
        for key in sle.keys():
            if key in line:
                x = line.index(key)
                sle[key] = (y,x)
    start, lever, end = sle["S"], sle["L"], sle["E"]
    to_lever = bfs(start, lever, field1)
    to_end = bfs(lever, end, field2)
    return (to_lever + to_end + 1) * (to_lever * to_end != 0) -1

def bfs(start, end, field):
    queue, answer = deque([start]), 0
    field[start[0]][start[1]] = 0
    while queue:
        (y,x) = queue.popleft()
        for (ny, nx) in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
            if (ny, nx) == end:
                answer = field[y][x] + 1
                break
            if nx >= 0 and ny >= 0 and ny < len(field) and nx < len(field[0]):
                if field[ny][nx] in ["O", "L", "E", "S"]:
                    field[ny][nx] = field[y][x] + 1
                    queue.append((ny, nx))
        if answer != 0:
            break
    return answer