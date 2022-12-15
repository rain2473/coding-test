def solution(clothes):
    type_clothes = []
    for i in range(len(clothes)):
        type_clothes.append(clothes[i][1])
    set_type = set(type_clothes)
    tmp = 1
    for case in set_type:
        tmp *= type_clothes.count(case)+1
    return tmp - 1