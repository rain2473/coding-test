def solution(board):
    count = 0
    for i,line in enumerate(board):
        for j, pos in enumerate(line):
            if pos == 1:
                board[i][j] = "지뢰"
                count += 1
                for k in range(i-1,i+2):
                    k = k*(k>-1) + (k>len(board)-1)*(len(board)-1-k)
                    for l in range(j-1,j+2):
                        l = l*(l>-1) + (l>len(board)-1)*(len(board)-1-l)
                        if board[k][l] == 0:
                                board[k][l] = "펑"
                                count += 1
    return len(board)**2 - count