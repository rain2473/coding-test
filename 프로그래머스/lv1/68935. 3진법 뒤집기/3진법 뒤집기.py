def solution(n):
    answer = 0
    i = 0
    while True:
        if 3 ** i > n:
            break
        i += 1
    for j in range(i):
        answer += (n//3**(i-j-1))*(3**j)*(n >= 3**(i-j-1))
        n = (n%3**(i-j-1))
    return answer