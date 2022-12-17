def solution(s):
    answer = 0
    tmp = 0
    for i in s.split(" "):
        try:
            answer += int(i)
            tmp = int(i)
        except:
            answer -= tmp
    return answer