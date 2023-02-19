def solution(k, d):
    answer, a, b = 0, 0, 0
    while (a) * k <= d:
        if b == 0:
            while (a * k) ** 2 + (b * k) ** 2 < d ** 2:
                b += 1
            if (a * k) ** 2 + (b * k) ** 2 != d ** 2:
                b -= 1
        else:
            while (a * k) ** 2 + (b * k) ** 2 > d ** 2:
                b -= 1
        answer += b + 1
        a += 1
    return answer