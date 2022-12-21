def solution(s):
    answer = 0
    if s[0] == ")" or s[-1] == "(":
        return False
    else:
        for i in range(len(s)):
            answer += (s[i] == "(") + (s[i] == ")")*-1
            if answer < 0:
                return False
        if answer != 0:
            return False
        else:
            return True