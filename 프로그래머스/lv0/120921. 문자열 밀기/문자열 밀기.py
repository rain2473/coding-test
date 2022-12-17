def solution(A, B):
    tmp = A *2
    answer = 0
    if B in tmp:
        for i in range(len(A)):
            if tmp[len(A)-i:2*len(A)-i] == B:
                answer =  i
                break
    else:
        answer = -1
    return answer