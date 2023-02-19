def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x:x[0], reverse = True)
    data.sort(key = lambda x:x[col-1])
    for i in range(row_begin, row_end+1):
        S = data[i-1]
        tmp = 0
        for j in S:
            tmp += (j % i)
        if i == row_begin:
            answer = tmp
        else:
            answer = answer ^ tmp
    return answer