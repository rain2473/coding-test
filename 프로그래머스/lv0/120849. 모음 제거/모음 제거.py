def solution(my_string):
    for i in list("aeiou"):
        my_string = my_string.replace(i,"")
    return my_string