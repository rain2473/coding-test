def solution(n):
    answer = [0 for i in range(n+1)]
    answer[0], answer[2] = 1, 3
    for k in range(4,n+1):
        answer[k] = answer[k-2] * 4 - answer[k-4]
    return answer[-1] % 1000000007