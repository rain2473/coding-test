def solution(sizes):
    max_w, max_h = 0, 0
    for card in list(map(sorted,sizes)):
        max_w += (card[0] - max_w) * (card[0] > max_w)
        max_h += (card[1] - max_h) * (card[1] > max_h)
    return max_w * max_h