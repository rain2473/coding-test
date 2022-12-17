def solution(my_string):
    answer, plus = [], 1
    for i in my_string.split(" "):
        try:
            answer.append(int(i)*plus)
        except:
            plus = -2 * (i == "-") + 1
    return sum(answer)