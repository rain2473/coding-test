def solution(name, yearning, photo):
    hashMap = {name[i]:yearning[i] for i in range(len(name))}
    answer = []
    for people in photo:
        tmp = 0
        for person in people:
            try:
                tmp += hashMap[person]
            except:
                continue
        answer.append(tmp)
    return answer