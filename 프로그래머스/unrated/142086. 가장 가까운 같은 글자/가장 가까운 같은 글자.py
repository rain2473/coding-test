def solution(s):
    check = {}
    answer = []
    for i,c in enumerate(s):
        try:
            answer.append(i - check[c])
        except:
            answer.append(-1)
        check[c] = i
    return answer