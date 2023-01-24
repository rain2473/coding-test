def trans(m, n, board):
    board_t = {j:[] for j in range(n)}
    for i in range(m):
        for j in range(n):
            board_t[j] += [board[i][j]]
    return board_t

def exe(m, n, answer, board_t):
    memory = []
    for x in range(n-1):
        col1 = board_t[x]
        col2 = board_t[x+1]
        for y in range(m-1):
            tmp = set([col1[y],col1[y+1],col2[y],col2[y+1]])
            if len(tmp) == 1 and tmp != set([" "]):
                memory.append([x,y])
    for x, y in memory:
        board_t[x][y], board_t[x][y+1], board_t[x+1][y], board_t[x+1][y+1] = "0","0","0","0"
    for col in range(len(board_t)):
        answer += board_t[col].count("0")
        tmp = "".join(board_t[col]).replace("0","")
        tmp = " " * (len(board_t[col])-len(tmp)) + tmp
        board_t[col] = list(tmp)
    return board_t, answer
 
def retrans(m,n,board_t):
    new_board = [["0"]*n]*m
    for col in range(len(board_t)):
        for i in range(m):
            new_board[i][col] = board_t[col][i]
    board = []
    for row in new_board:
        board.append("".join(row))
    return board

def solution(m, n, board):
    answer = 0
    board_t = trans(m, n, board)
    while True:
        board_t, new_answer = exe(m, n, answer, board_t)
        if new_answer == answer:
            break
        answer = new_answer
    board = retrans(m,n,board_t)
    return answer

