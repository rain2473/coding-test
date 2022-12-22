def solution(n, m):
    answer = 0
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            answer = i
            break
    return [answer, n*m//answer]