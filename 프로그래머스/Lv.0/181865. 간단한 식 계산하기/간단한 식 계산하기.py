def solution(binomial):
    sep = binomial.split(" ")
    if sep[1] == "+":
        answer = int(sep[0]) + int(sep[2])
    elif sep[1] == "-":
        answer = int(sep[0]) - int(sep[2])
    else:
        answer = int(sep[0]) * int(sep[2])
    return answer