def solution(n):
    k, count  = 1, 0
    while True:
        if n - k*(k-1)//2 <= 0:
            break
        else:
            count += ((n - k*(k-1)//2) % k == 0)*1
        k += 1
    return count