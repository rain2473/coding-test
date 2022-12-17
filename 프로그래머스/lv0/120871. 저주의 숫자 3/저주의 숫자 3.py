def solution(n):
    answer = []
    i = 1
    while len(answer)!=n:
        if "3" not in str(i) and (i)%3!=0:
            answer.append(i)
        i += 1
    return answer[-1]