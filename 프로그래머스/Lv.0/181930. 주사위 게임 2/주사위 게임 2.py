def solution(a, b, c):
    answer = 1
    for i in range(1, 5 - len(set([a, b, c]))):
        answer *= (a ** i + b ** i + c ** i)
    return answer