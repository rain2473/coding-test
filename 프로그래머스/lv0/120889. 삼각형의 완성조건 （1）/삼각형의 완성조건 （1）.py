def solution(sides):
    return 2 - (sorted(sides)[2] < sorted(sides)[1]+sorted(sides)[0])