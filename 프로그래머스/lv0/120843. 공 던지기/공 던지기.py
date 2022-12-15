def solution(numbers, k):
    n = len(numbers)
    answer = [i*2+1 for i in range(n//2)] * (1+(n % 2 == 0)) + ((n % 2 != 0))*([n] + [i*2 for i in range(1,n//2+1)])
    return answer[k%n-1]