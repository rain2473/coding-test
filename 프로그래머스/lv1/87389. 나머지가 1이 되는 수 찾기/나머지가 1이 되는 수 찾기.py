def solution(n):
    answer = 0
    for i in range(2,int((n-1)**0.5)+1):
        if n % i ==1:
            answer = i
            break
    return (answer-n+1) * (answer != 0) + (n-1)