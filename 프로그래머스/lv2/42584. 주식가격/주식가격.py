from collections import deque
def solution(prices):
    answer, prices = [], deque(prices)
    while prices:
        price, second = prices.popleft(), 0
        for i in prices:
            second += 1
            if price > i:
                break
        answer.append(second)
    return answer