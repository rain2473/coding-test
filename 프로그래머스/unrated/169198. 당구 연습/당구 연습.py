def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        [x, y] = ball
        reflecteds = [[x , -y],[-x , y],[2 * m - x , y],[x , 2 * n - y]]
        if startX == x:
            reflecteds = [[-x , y],[2 * m - x , y]]
            if startY > y:
                reflecteds.append([x , 2 * n - y])
            else:
                reflecteds.append([x , - y])
        if startY == y:
            reflecteds = [[x , -y],[x , 2 * n - y]]
            if startX > x:
                reflecteds.append([2 * m - x , y])
            else:
                reflecteds.append([-x, y])
        distance = m ** 2 + n ** 2 * 4
        for reflected in reflecteds:
            tmp = (startX - reflected[0])  ** 2 + (startY - reflected[1])  ** 2
            if distance > tmp:
                distance = tmp
        answer.append(distance)
    return answer