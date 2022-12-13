def solution(array, n):
    answer = 0
    for _ in sorted(array):
        if _ == n:
            answer += 1
        elif _ > n:
            break
    return answer