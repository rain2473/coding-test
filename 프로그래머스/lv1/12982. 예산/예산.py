def solution(d, budget):
    d = sorted(d)
    while True:
        if sum(d) <= budget:
            break
        d = d[:-1]
    return len(d)