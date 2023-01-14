from collections import deque
def solution(rows, columns, queries):
    answer, matrix, queries = [], [], deque(queries)
    for i in range(rows):
        tmp = [j+1 +columns*i for j in range(columns)]
        matrix.append(tmp)
    while queries:
        query = queries.popleft()
        rc = get_part(matrix,query)
        rc,small = rotate(rc)
        matrix = change(matrix,query,rc)
        answer.append(small)
    return answer

def get_part(matrix,query):
    result = []
    for i in range(query[0]-1,query[2]):
        tmp = matrix[i][query[1]-1:query[3]]
        result.append(tmp)
    return result

def change(matrix,query,rc):
    for i in range(query[0]-1,query[2]):
        matrix[i] = matrix[i][:query[1]-1] +rc[i-query[0]+1] +matrix[i][query[3]:]
    return matrix

def rotate(rc):
    top, bottom, left, right, around = rc[0], rc[-1], [], [], []
    for j in range(len(rc)):
        right.append(rc[j][-1])
        left.append(rc[j][0])
    around = top + right[1:-1] + bottom[::-1] + left[1:-1][::-1]
    around = [around[-1]] + around[:-1]
    top = around[:len(rc[0])]
    right = around[len(rc[0])-1:len(rc[0])+len(rc)-1]
    bottom = around[len(rc[0])+len(rc)-2:2*len(rc[0])+len(rc)-2][::-1]
    left = [around[0]]+around[-len(rc)+1:][::-1]
    for i in range(len(rc)):
        rc[i][0] = left[i]
        rc[i][-1] = right[i]
    rc[0] = top
    rc[-1] = bottom
    return rc, min(around)