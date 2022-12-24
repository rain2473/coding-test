def solution(board, moves):
    answer, basket = 0, [0]
    for i in moves:
        for row in board:
            if row[i-1] != 0:
                if basket[-1] != (row[i-1]):
                    basket.append(row[i-1])
                else:
                    answer += 2
                    basket.pop()
                row[i-1] = 0
                break
    return answer