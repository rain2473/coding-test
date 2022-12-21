def solution(food):
    new_food = [i//2 for i in food]
    answer = ''
    for i,m in enumerate(new_food):
        answer += str(i)*m
    return answer+"0"+answer[::-1]