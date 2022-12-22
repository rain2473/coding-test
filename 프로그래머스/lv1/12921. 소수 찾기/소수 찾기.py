def solution(n):
    answer = []
    for i in range(2,n+1):
        tmp = 0
        for j in range(2,int(n**0.5)+1):
            if i % j ==0 and i != j:
                tmp = 1
                break
        if tmp == 0:
            answer.append(i)
    return len(answer)