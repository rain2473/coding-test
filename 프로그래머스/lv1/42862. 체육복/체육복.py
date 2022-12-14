def solution(n, lost, reserve):
    _lost = sorted(list(set(lost) - set(reserve)))
    _reserve = sorted(list(set(reserve) - set(lost)))
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)