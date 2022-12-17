def solution(n):
    answer = []
    for i in range(2,n+1):
        if n % i == 0:
            answer.append(i)
            for j in range(2,i):
                if i%j == 0:
                    answer.pop()
                    break
    return answer