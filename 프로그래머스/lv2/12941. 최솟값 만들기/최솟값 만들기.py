def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B)[::-1]
    while len(A) != 0:
        answer += A.pop(0)*B.pop(0)
    return answer