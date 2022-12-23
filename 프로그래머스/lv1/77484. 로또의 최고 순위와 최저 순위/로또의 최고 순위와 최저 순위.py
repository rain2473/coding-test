def solution(lottos, win_nums):
    maximum = len(set(lottos)-set(win_nums+[0]))
    maximum += 1*(maximum<6)
    minimum = lottos.count(0) + maximum
    minimum -= 1*(minimum>6)
    return [maximum,minimum]