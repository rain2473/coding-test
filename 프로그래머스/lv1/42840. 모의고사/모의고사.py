def solution(answers):
    answer, score = [], []
    first = ("12345"*(len(answers)//5+1))[:len(answers)]
    second = ("21232425"*(len(answers)//8+1))[:len(answers)]
    third = ("3311224455"*(len(answers)//10+1))[:len(answers)]
    for i in [first, second, third]:
        tmp = 0
        for j in range(len(answers)):
            tmp += (answers[j] == int(i[j]))
        score.append(tmp)
    for i,k in enumerate(score):
        if k == max(score):
            answer.append(i+1)
    return answer