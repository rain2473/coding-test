def solution(board):
    size = 0
    new_board = {i:{} for i in range(len(board))}

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 0:
                new_board[i][j] = 0
                continue
            if min(i, j) == 0:
                new_board[i][j] = 1
            else:                
                new_board[i][j] = min(new_board[i-1][j-1], new_board[i-1][j], new_board[i][j-1]) + 1
            
            size = max(size, new_board[i][j])
    
    return size ** 2