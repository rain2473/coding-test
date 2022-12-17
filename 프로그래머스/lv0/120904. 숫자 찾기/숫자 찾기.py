def solution(num, k):
    answer = -1
    for i,j in enumerate(str(num)):
        if int(j) == k:
            answer = i+1
            break
    return answer