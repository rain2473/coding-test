def solution(m, n, puddles):
    m, n = m-1, n-1
    field = [[0 for i in range(m+1)] for j in range(n+1)]
    field[0][0] = 1
    for y in range(n+1):
        for x in range(m+1):
            if [x+1,y+1] in puddles or x + y == 0:
                continue
            else:
                field[y][x] = field[y-1][x] + field[y][x-1]
    return field[-1][-1] % 1000000007