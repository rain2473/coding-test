def solution(lines):
    tmp = []
    answer = 0
    for line in lines:
        for i in range(line[1]-line[0]):
            tmp.append(str(line[0]+i)+str(line[0]+1+i))
    for i in set(tmp):
        if tmp.count(i) > 1:
            answer += 1
    return answer