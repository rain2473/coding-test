def solution(n):
    tmp = [0 for j in range(n+1)]
    tmp[1] = 1
    if n >2:
        for i in range(2,n+1):
            tmp[i] = (tmp[i-1]+ tmp[i-2])%1234567
    answer = tmp[n]
    return answer