def solution(strArr):
    answer = []
    for i, st in enumerate(strArr):
        if i % 2 == 0:
            st = st.lower()
        else:
            st = st.upper()
        answer.append(st)
    return answer