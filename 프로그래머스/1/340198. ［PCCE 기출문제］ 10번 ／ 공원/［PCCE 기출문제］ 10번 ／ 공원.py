def solution(mats, park):
    mats = reversed(sorted(mats))
    park_h = len(park)
    park_w = len(park[0])
    answer = -1
    point = 0
    for mat in mats:
        tmp = 0
        if mat > park_h or mat > park_w:
            continue
        for i in range(park_h - mat + 1):
            for j in range(park_w - mat + 1):                
                for row in park[i : i + mat]:
                    try:
                        tmp += sum(list(map(int, row[j : j + mat])))
                        answer = mat
                        point += 1
                        if point == mat:
                            return point
                    except:
                        answer = -1
                        point = 0
                        break
        
    return answer