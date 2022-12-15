def solution(my_string):
    answer = []
    for i in list(my_string):
        try:
            answer.append(int(i))
        except:
            continue
    return sorted(answer)