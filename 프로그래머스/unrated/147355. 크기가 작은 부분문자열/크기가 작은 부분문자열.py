def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if t[i] != 0:
            answer += (int(t[i:i+len(p)]) <= int(p))
    return answer