def solution(arr1, arr2):
    answer = []
    for arr1_row in arr1:
        tmp = [0 for _ in range(len(arr2[0]))]
        for i,a in enumerate(arr1_row):
            for j in range(len(arr2[0])):
                tmp[j] += a * arr2[i][j]
        answer.append(tmp)
    return answer
            
        