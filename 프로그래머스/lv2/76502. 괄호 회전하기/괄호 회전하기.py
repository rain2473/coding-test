def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        cop = s
        while True:
            switch = 0
            tmp = cop.replace("()","")
            tmp = tmp.replace("{}","")
            tmp = tmp.replace("[]","")
            if cop != tmp:
                cop = tmp
                switch = 1
            if switch == 0:
                break
        if cop == "":
            answer += 1
    return answer