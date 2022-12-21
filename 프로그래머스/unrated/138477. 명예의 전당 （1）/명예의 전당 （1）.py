def solution(k, score):
    answer = []
    for i in range(len(score)):
        answer.append(sorted(score[:i+1],reverse = True)[:k][-1])
    return answer