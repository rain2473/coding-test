def solution(N, stages):
    answer, fail, tmp = [], {}, 0
    for i in range(1,N+1):
        try:
            fail[i] = stages.count(i) / (len(stages) - tmp)
        except:
            fail[i] = 0
        tmp += stages.count(i)
    for i in sorted(fail.items(), key = lambda x : x[1], reverse = True):
        answer.append(i[0])
    return answer