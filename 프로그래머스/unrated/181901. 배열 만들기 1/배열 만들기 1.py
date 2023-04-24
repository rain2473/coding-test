def solution(n, k):
    i = 0
    answer = []
    while i <= n:
        if i != 0:
            answer.append(i)
        i += k
    return answer