from itertools import combinations
def solution(line):
    result = set()
    answer = []
    minx, miny = float("inf"), float("inf")
    maxx, maxy = -float("inf"), -float("inf")
    for comb in list(combinations(line,2)):
        denom = (comb[0][1] * comb[1][0] - comb[0][0] * comb[1][1])
        if denom == 0:
            continue
        y = (comb[0][0] * comb[1][2] - comb[0][2] * comb[1][0]) / denom
        x = (comb[0][2] * comb[1][1] - comb[0][1] * comb[1][2]) / denom
        if y == int(y) and x == int(x):
            x,y = int(x), int(y)
            result.add((x,y))
            minx = int(min(minx, x))
            miny = int(min(miny, y))
            maxx = int(max(maxx, x))
            maxy = int(max(maxy, y))
    answer = [["." for i in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
    while result:
        [tmpx, tmpy] = result.pop()
        [tmpx, tmpy] = [tmpx - minx, maxy - tmpy]
        answer[tmpy][tmpx] = "*"
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    return answer