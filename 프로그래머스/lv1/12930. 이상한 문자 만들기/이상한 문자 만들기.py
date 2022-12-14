def solution(s):
    answer = []
    s = s.split(" ")
    for word in s:
        word = list(word)
        for i,c in enumerate(word):
            if i % 2 == 0:
                c = c.upper()
            else:
                c = c.lower()
            answer.append(c)
        answer.append(" ")
    answer = "".join(answer[:-1])
    return answer