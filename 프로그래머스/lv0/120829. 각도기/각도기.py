import math
def solution(angle):
    answer = 0
    answer = 2*(angle // 90) + (angle % 90 != 0)
    return answer