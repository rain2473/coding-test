def solution(s):
    answer, tmp = [], {}
    for c in s[2:-2].split("},{"):
        tmp[len(list(map(int,c.split(","))))] = list(map(int,c.split(",")))
    for c in sorted(tmp):
        for i in tmp[c]:
            if answer.count(i) == 0:
                answer.append(i)
    return answer