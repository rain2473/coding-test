def solution(n):
    answer,i = 1,1
    while True:
        if n < answer:
            break
        else:
            answer *= i
            i += 1
    return i-2