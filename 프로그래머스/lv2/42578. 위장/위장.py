def solution(clothes):
    answer = 1
    type_clothes = [clothes[i][1] for i in range(len(clothes))]
    for case in set(type_clothes):
        answer *= type_clothes.count(case)+1
    return answer - 1