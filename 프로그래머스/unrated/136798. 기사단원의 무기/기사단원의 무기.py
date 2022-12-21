def solution(number, limit, power):
    answer = []
    for i in range(1,number+1):
        tmp = (int(i**0.5)**2==i)*-1
        for j in range(1,int(i**0.5)+1):
            if i%j == 0:
                tmp += 2
        tmp = (power-tmp)*(tmp > limit) + tmp
        answer.append(tmp)
    return sum(answer)