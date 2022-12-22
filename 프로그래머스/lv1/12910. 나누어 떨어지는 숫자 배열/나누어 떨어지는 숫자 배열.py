def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    return sorted(answer) + [-1]*(len(answer)==0)