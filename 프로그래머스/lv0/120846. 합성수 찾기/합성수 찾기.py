def solution(n):
    answer = 0
    if n > 2:
        for i in range(2,n+1):
            for j in range(2,i):
                if i % j ==0:
                    answer += 1
                    break
        return answer    
    else:
        return 0