def solution(dartResult):
    answer = []
    dartResult = dartResult.replace("10","A")
    for i in dartResult:
        if i in list("0123456789") or i == "A":
            try:
                answer.append(tmp)
            except:
                pass
            try:
                tmp = int(i)
            except:
                tmp = 10
        elif i in ["*","#"]:
            tmp = tmp * (2*(i == "*")+-1*(i == "#"))
            try:
                answer[-1] += answer[-1]*(i == "*")
            except:
                pass
        elif i in ["S","D","T"]:
            tmp = tmp ** ((i == "S")+2*(i == "D")+3*(i == "T"))
    answer.append(tmp)
    return sum(answer)