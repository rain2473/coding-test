def solution(n):
    answer = [1 for i in range(n+1)]
    for i in range(2,n+1):
        answer[i] = (answer[i-1] + answer[i-2]) % 1000000007
    return answer[n]