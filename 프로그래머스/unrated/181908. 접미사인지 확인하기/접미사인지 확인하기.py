def solution(my_string, is_suffix):
    answer = my_string[::-1].replace(is_suffix[::-1], "^")
    return (answer[0] == "^") * 1