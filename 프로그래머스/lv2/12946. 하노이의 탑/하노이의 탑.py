def solution(n):
    answer = hanoi(n,1,2,3)
    return answer

def hanoi(n,a,b,c):
    if n == 1:
        answer = [[a, c]]
    else:
        answer = hanoi(n-1,a,c,b) + [[a,c]] + hanoi(n-1,b,a,c)
    return answer