from collections import defaultdict
def solution(weights):
    answer, info = 0, defaultdict(int)
    for w in weights:
        answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3]
        answer += info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
        info[w] += 1
    return answer