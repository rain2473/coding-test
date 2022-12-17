def solution(dots):
    x = []
    y = []
    for pos in dots:
        x.append(pos[0])
        y.append(pos[1])
    return (max(x)-min(x))*(max(y)-min(y))