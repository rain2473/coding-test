def solution(today, terms, privacies):
    answer, tmp = [], {}
    for i in terms:
        tmp[i.split(" ")[0]] = i.split(" ")[1]
    terms = tmp
    
    for i, id in enumerate(privacies):
        temp = list(map(int,id.split(" ")[0].split(".")))
        temp[1] = temp[1] + int(terms[id.split(" ")[1]]) - (temp[2]==1)
        temp[0] = str(temp[0] + temp[1] // 12 - (temp[1] % 12 == 0))
        temp[1] = str(temp[1] % 12 + 12 * (temp[1] % 12 == 0)).zfill(2)
        temp[2] = str(temp[2] - 1 + 28*(temp[2]==1)).zfill(2)
        if int("".join(temp)) < int("".join(today.split("."))):
            answer.append(i+1)
    return answer 