def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        answer += i + (int(i**0.5)**2 == i)*-2 * i
    return answer