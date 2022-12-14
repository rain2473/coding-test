def solution(n, lost, reserve):
    new_lost = sorted(list(set(lost) - set(reserve))) # 새로 선언. 덧씌우면 문제발생
    new_reserve = sorted(list(set(reserve) - set(lost))) # 새로 선언. 덧씌우면 문제발생
    # 2열의 lost를 덧 씌우면, 아래 3열의 reserve를 선언하는 것에 영향을 줌
    for i in new_reserve:
        if i - 1 in new_lost:
            new_lost.remove(i - 1)
        elif i + 1 in new_lost:
            new_lost.remove(i + 1)
    return n - len(new_lost)