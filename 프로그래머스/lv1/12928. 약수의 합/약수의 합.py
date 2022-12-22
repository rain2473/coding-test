def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            answer += i + n//i
    return answer - (int(n**0.5)**2==n)*int(n**0.5)