def solution(dots):
    answer = []
    for i, p1 in enumerate(dots):
        for j, p2 in enumerate(dots):
            if i != j:
                answer.append((p1[1]-p2[1])/(p1[0]-p2[0]))
    return (len(set(answer))!=6)*1