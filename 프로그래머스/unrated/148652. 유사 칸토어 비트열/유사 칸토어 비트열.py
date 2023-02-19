def solution(n, l, r):
    def sol(num):
        if num <= 5: 
            return '11011'[:num].count('1')
        digit = 0
        while 5 ** (digit + 1) < num:
            digit += 1
        q = num // (5 ** digit)
        re = num % (5 ** digit)
        answer = q * (4 ** digit)
        if q > 2:
            answer -= (4 ** digit)
        if q == 2:
            return answer
        else:
            return answer + sol(re)
    return sol(r) - sol(l - 1)