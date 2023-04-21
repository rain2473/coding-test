def solution(my_string, is_prefix):
    my_string = my_string.replace(is_prefix,"$")
    return (my_string[0] == "$") * 1