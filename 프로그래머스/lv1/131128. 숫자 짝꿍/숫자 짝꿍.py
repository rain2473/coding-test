def solution(X, Y):
    X = str(X)
    Y = str(Y)
    intersection = []
    for i in range(10):
        intersection += [i] * min(X.count(str(i)), Y.count(str(i)))
    if list(set(intersection)) == [0]:
        return "0"
    elif len(intersection) == 0:
        return "-1"
    else:
        return "".join(list(map(str,sorted(intersection,reverse = True))))