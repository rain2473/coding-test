def solution(price):
    return int(price*(1-0.05*((price >= 100000) + (price >= 300000) + (price >= 500000)*2)))