def solution(board):
    O , X = [], []
    def win(X):
        win = [((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0))]
        for x in range(3):
            tmp = []
            for y in range(3):
                tmp.append((x,y))
            tmp = tuple(tmp)
            win.append(tmp)
        for y in range(3):
            tmp = []
            for x in range(3):
                tmp.append((x,y))
            tmp = tuple(tmp)
            win.append(tmp)
        for case in win:
            if set(case) & set(X) == set(case):
                return True
        return False
        
    for y, line in enumerate(board):
        for x, _ in enumerate(line):
            if _ == "O":
                O.append((x,y))
            elif _ == "X":
                X.append((x,y))
    if len(X) > len(O) or len(O) > len(X) + 1:
        return 0
    if win(O) and len(O) == len(X):
        return 0
    if win(X) and len(O) > len(X):
        return 0
    answer = 1
    return answer