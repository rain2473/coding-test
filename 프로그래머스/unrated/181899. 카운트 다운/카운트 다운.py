def solution(start, end):
    answer = [i for i in range(end, start  + 1)][::-1]
    return answer