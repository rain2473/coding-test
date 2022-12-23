def solution(strings, n):
    answer, order = [], []
    for i in strings:
        order.append(i[n])
    for c in sorted(set(order)):
        tmp = []
        for i in strings:
            if i[n] == c:
                tmp.append(i)
        answer += sorted(tmp)
    return answer