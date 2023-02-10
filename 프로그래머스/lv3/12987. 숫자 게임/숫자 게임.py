from collections import deque
def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B = deque(sorted(B))
    while B:
        a = A.pop()
        b = B.popleft()
        if b > a:
            answer += 1
        else:
            A.append(a)
    return answer