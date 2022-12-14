def solution(my_string, letter):
    answer = ""
    for n in list(my_string):
        if n != letter:
            answer += n
    return answer