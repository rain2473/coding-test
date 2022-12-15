def solution(n):
    return sum([2*(n % i == 0) for i in range(1,int(n**0.5)+1)]) - (int(n**0.5)**2==n)