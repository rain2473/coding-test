def solution(n):
    answer = ''
    for i in range(n):
        answer += "수"*(i%2 !=1)+"박"*(i%2 !=0)
    return answer