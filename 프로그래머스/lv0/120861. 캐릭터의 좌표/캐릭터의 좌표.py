def solution(keyinput, board):
    x, y, z, w = 0, 0, board[0]//2, board[1]//2
    for key in keyinput:
        if (abs(x) <= z):
            tmp = (key=="left")*-1+(key=="right")
            x = (abs(tmp+x) <= z)*tmp + x
        if (abs(y) <= w):
            tmp = (key=="up")+-1*(key=="down")
            y = (abs(tmp+y) <= w)*tmp + y
    return [x,y]