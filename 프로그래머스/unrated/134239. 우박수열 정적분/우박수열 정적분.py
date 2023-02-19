def solution(k, ranges):
    hail, area, answer = [], [], []
    while k != 1:
        hail.append(k)
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        s = (hail[-1] + k) / 2
        area.append(s)
    for [i, j] in ranges:
        if i <= len(area)+j:
            tmp = sum(area[i: len(area)+j])
        else:
            tmp = -1.0
        answer.append(tmp)
    return answer