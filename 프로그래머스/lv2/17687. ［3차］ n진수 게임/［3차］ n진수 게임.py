def solution(n, t, m, p):
    total, answer, idx, p = '', '', 0, p-1
    while len(total) <= t*m:
        total += mod_n(n, idx)
        idx += 1
    for i in range(t):
        answer += total[i*m+p]
    return answer

def mod_n(n, k):
    num = "0123456789ABCDEF"
    answer = ""
    if k == 0:
        return "0"
    while k != 0:
        answer += num[k % n]
        k = k // n
    return answer[::-1]