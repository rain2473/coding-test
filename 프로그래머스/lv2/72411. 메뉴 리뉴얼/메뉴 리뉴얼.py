from itertools import combinations
def solution(orders, course):
    answer, count = {x:[] for x in course}, {x:0 for x in course}
    combi = sum(list(map(ex,list(combinations(orders,2)))),[])
    for com in set(combi):
        if len(com) in course:
            if count[len(com)] == combi.count(com):
                answer[len(com)] += [com]
            elif combi.count(com) > count[len(com)]:
                answer[len(com)] = [com]
                count[len(com)] = combi.count(com)
    answer = sum(answer.values(),[])
    return sorted(answer)

def ex(ls):
    a, b = set(ls[0]), set(ls[1])
    answer = "".join(sorted(list(a & b)))
    if len(answer) > 1:
        result = []
        for i in range(2,len(answer)+1):
            result += list(map(set_to_string,combinations(answer,i)))
        return result
    else:
        return []
    
def set_to_string(a):
    return "".join(a)