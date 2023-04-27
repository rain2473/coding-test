def solution(n):
    answer = 0
    for i in range(n//2 + 1):
        answer += (4 * i ** 2) * (n % 2 == 0) + (2 * i + 1) * (n % 2 != 0)
    return answer