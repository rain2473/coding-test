import math
def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        y1 = math.floor((r2 ** 2 - x ** 2) ** 0.5)
        y2 = ((x <= r1) * (r1 ** 2 - x ** 2)) ** 0.5
        y2 = math.floor(y2)- (y2 == math.floor(y2))
        answer += y1 - y2
    answer *= 4
    return answer