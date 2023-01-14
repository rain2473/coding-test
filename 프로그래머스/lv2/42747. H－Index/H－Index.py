def solution(citations):
    answer, citations = len(citations), sorted(citations,reverse=True)
    for i, c in enumerate(citations):
        if i>=c:
            answer = i
            break
    return answer