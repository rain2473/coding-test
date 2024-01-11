def solution(my_string, m, c):
    answer = [my_string[c - 1 + m * i] for i in range(len(my_string) // m)]
    return "".join(answer)