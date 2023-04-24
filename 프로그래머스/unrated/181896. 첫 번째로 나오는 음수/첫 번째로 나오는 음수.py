def solution(num_list):
    answer = -1
    for i, n in enumerate(num_list):
        if n < 0:
            return i
    return answer