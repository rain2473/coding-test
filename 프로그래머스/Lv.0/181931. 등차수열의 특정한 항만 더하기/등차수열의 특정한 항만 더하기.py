def solution(a, d, included):
    answer = []
    for i, x in enumerate(included):
        if x:
            answer.append(i)
    return a * len(answer) + d * sum(answer)