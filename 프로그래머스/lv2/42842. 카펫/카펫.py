def solution(brown, yellow):
    sidelen = []
    for i in range(1,int(yellow**0.5)+1):
        if yellow % i == 0:
            sidelen.append([i, yellow//i])
    for i in sidelen:
        if brown + yellow == (i[0]+2) * (i[1]+2):
            return sorted([(i[0]+2),(i[1]+2)], reverse =True)
            break