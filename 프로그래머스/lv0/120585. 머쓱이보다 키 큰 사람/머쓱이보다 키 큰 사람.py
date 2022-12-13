def solution(array, height):
    answer = 0
    array = sorted(array)[::-1]
    for _ in array:
        if _ > height:
            answer += 1
        else:
            break
    return answer