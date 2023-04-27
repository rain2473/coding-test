def solution(str_list, ex):
    answer = ''
    for str_ in str_list:
        if ex in str_:
            continue
        answer += str_
    return answer