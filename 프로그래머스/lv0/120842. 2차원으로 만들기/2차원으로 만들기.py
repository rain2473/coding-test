def solution(num_list, n):
    answer = []
    tmp = []
    for m in num_list:
        tmp.append(m)
        if len(tmp) == n:
            answer.append(tmp)
            tmp = []
    return answer