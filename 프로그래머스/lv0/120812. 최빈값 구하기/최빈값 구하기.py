def solution(array):
    max_count = 0
    mod_num = 0
    counter = set(array)
    for c in counter:
        if max_count < array.count(c):
            max_count = array.count(c)
            mod_num = c
        elif max_count == array.count(c) and mod_num != c:
            mod_num = -1
    return mod_num