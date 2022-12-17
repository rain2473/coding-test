def solution(numlist, n):
    temp, plus = {}, {}
    for i in numlist:
        temp[i] = abs(i-n)
        plus[i] = 2*(abs(i-n)==(i-n))-1
    tmp = sorted(temp.values())
    for i in range(len(tmp)):
        for j in temp.keys():
            if temp[j] == tmp[i]:
                tmp[i] *= plus[j]
                break
        try: 
            if abs(tmp[i]) == abs(tmp[i-1]):
                tmp[i-1] = +abs(tmp[i])
                tmp[i] = -abs(tmp[i])
        except:
            continue
    return [i+n for i in tmp]
    # return sorted(numlist,key = lambda x: [abs(x-n),-x])