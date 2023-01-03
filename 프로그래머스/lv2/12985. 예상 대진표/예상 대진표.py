def solution(n,a,b):
    answer = 1
    while True:
        if (a-1)//2 == (b-1)//2:
            break
        else:
            answer += 1
            a = (a-1)//2 + 1
            b = (b-1)//2 + 1
    return answer