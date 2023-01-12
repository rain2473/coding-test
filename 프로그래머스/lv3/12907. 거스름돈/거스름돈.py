def solution(n, money):
    answer = [1] + [0 for i in range(n)]
    for coin in sorted(money):
        for i in range(coin, n+1):
            answer[i] += answer[i - coin]
    return answer[n] % 1000000007