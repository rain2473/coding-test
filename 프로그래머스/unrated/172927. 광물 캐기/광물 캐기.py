from collections import deque
def solution(picks, minerals):
    answer = 0
    picks = ["diamond"] * picks[0] + ["iron"] * picks[1] + ["stone"] * picks[2]
    seted_minerals, tmp = [], []
    minerals = deque(minerals)
    while minerals:
        tmp.append(minerals.popleft())
        if len(tmp) == 5 or len(minerals) == 0:
            tmp = [tmp.count("diamond"), tmp.count("iron"), tmp.count("stone")]
            seted_minerals.append(tmp)
            tmp = []
    seted_minerals = seted_minerals[:len(picks)]
    seted_minerals.sort(reverse = True, key = lambda x : (x[0], x[1]))
    picks = deque(picks)
    seted_minerals = deque(seted_minerals)
    while picks and seted_minerals:
        pick = picks.popleft()
        mineral = seted_minerals.popleft()
        diamond = mineral[0]
        iron = mineral[1]
        stone = mineral[2]
        if pick == "diamond":
            answer += diamond + iron + stone
        elif pick == "iron":
            answer += 5 * diamond + iron + stone
        else:
            answer += 25 * diamond + 5 * iron + stone
    return answer