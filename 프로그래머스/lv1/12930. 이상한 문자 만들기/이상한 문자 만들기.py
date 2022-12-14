def solution(s):
    answer = []
    s = s.split(" ")
    for word in s:
        word = list(word)
        for i in range(len(word)):
            if i % 2 == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
        word = "".join(word)
        answer.append(word)
    answer = " ".join(answer)
    return answer