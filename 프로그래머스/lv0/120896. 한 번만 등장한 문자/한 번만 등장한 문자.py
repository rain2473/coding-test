def solution(s):
    answer = []
    for c in set(sorted(s)):
        if s.count(c) == 1:
            answer.append(c)
    return "".join(sorted(answer))