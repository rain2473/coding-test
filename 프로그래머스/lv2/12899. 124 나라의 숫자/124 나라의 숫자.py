def solution(n):
    answer = ''
    while n != 0:
        answer += str(n % 3) * (n % 3 != 0) + "4" * (n % 3 == 0)
        n = n // 3 - (n % 3 == 0)
    answer = answer[::-1]
    return answer