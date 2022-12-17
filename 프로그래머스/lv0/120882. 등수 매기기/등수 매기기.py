def solution(score):
    score = [sum(i) for i in score]
    answer = sorted([[score[i],i] for i in range(len(score))], reverse = 1)
    tmp, count = 1,1
    for i in range(len(score)):
        tmp += (answer[i][0]<answer[i-1][0])*(count)
        count = (count)*(answer[i][0]==answer[i-1][0])+1
        score[answer[i][1]] = tmp
    return score