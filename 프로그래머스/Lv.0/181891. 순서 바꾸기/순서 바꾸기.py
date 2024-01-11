def solution(num_list, n):
    front = num_list[n :]
    back = num_list[: n]
    return front + back