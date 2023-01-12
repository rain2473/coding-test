from itertools import permutations
def solution(k, dungeons):
    roots, answer = list(permutations(dungeons,len(dungeons))), []
    for root in roots:
        life, clear = k, 0
        for dungeon in root:
            if life >= dungeon[0]:
                clear += 1
                life -= dungeon[1]
            else:
                break
        answer.append(clear)
    return max(answer)