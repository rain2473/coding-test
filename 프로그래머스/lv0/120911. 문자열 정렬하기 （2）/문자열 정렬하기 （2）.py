def solution(my_string):
    return "".join(sorted(list(map(str.lower,list(my_string)))))
