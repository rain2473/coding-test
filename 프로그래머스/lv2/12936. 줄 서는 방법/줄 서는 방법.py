def solution(n, k):
    answer, fac, list_n, k = [], 1, [1], k-1
    for i in range(n-1):
        fac *= i+1
        list_n.append(i+2)
    while list_n:
        tmp = list_n.pop(k // fac)
        answer.append(tmp)
        k = (k % fac)
        if fac == 1:
            break
        else:
            fac = fac // len(list_n)
    return answer + list_n