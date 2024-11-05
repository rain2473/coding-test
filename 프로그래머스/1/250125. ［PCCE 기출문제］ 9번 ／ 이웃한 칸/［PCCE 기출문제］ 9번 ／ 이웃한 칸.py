def solution(board, h, w):
    answer = 0
    for tmp in [[h-1,w], [h+1,w], [h,w+1], [h,w-1]]:
        if tmp[0] == -1 or tmp[1] == -1 :
            continue
        try:
            answer += (board[tmp[0]][tmp[1]] == board[h][w])
        except:
            pass
    return answer