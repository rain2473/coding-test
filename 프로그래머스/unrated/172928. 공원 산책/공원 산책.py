from collections import deque
def solution(park, routes):
    routes = deque(routes)
    answer = []
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] == "S":
                answer = [y,x]
                break
    while (routes):
        x, y = answer[1], answer[0]
        tmp = routes.popleft().split(" ")
        command, length = tmp[0], int(tmp[1])
        check = 0
        for i in range(length):
            if command =="S":
                y += 1
            elif command == "E":
                x += 1
            elif command == "W":
                x -= 1
                if x < 0:
                    check = 1
                    break
            elif command == "N":
                y -= 1
                if y < 0:
                    check = 1
                    break
            try:
                if park[y][x] == "X":
                    check = 1
                    break
            except:
                check = 1
                break
        if check != 1:
            answer = [y, x]
    return answer