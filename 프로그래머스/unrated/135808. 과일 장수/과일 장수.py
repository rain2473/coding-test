def solution(k, m, score):
    score = sorted(score, reverse = True)
    answer = 0
    for i in range(len(score)//m):
        answer += min(score[m*i:m*(i+1)])*m
    return answer