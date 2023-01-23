def solution(n):
    answer = [[0 for i in range(j+1)] for j in range(n)]
    num, x, y, snail = 1, -1, 0, 0
    while snail != n:
        for j in range(n-snail):
            if snail % 3 == 0:
                x += 1
            elif snail % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
        snail += 1
    answer = sum(answer,[])
    return answer