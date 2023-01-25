def solution(triangle):
    for i in range(len(triangle)-2,-1,-1):
        triangle[i] = in_to_sum(triangle, i+2)
    triangle = sum(triangle,[])
    return triangle[0]

def in_to_sum(triangle, k):
    answer = []
    row1 = triangle[k-2]
    row2 = triangle[k-1]
    for i in range(k-1):
        tmp = max(row1[i] + row2[i], row1[i] + row2[i+1])
        answer.append(tmp)
    return answer