def solution(s):
    answer = []
    while len(s) != 0:
        switch = 0
        for i in range(1,len(s)//2+1):
            if s[0:i*2].count(s[0]) == i:
                answer.append(s[0:i*2])
                s = s[i*2:]
                switch = 1
                break
        if switch == 0:
            answer.append(s)
            s = ""
    return len(answer)