def solution(order):
    answer = 0
    for coffee in order:
        if 'latte' in coffee:
            answer += 500
        answer += 4500
    return answer