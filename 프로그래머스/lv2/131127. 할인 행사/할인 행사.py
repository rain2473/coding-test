def solution(want, number, discount):
    answer, idx = 0, 0
    while idx <= len(discount):
        tmp, swt = discount[idx:idx+10], 1
        for i in range(len(want)):
            if tmp.count(want[i]) != number[i]:
                swt = 0
                break
        if swt == 1:
            answer += 1
        idx += 1
        
    return answer