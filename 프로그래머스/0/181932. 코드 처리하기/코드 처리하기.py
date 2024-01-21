def solution(code):
    answer = ''
    mode = 0
    for i, x in enumerate(code):
        if x == '1':
            mode = (mode == 0) * 1
            continue
        if mode == 0:
            if i % 2 == 0:
                answer += x
        elif i % 2 != 0:
                answer += x
    if answer == '':
        answer = 'EMPTY'
    return answer