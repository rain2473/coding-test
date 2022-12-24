def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = str(bin(arr1[i] | arr2[i]))[2:].replace("1","#")
        tmp = tmp.replace("0"," ")
        while len(tmp) < n:
            tmp = " "+tmp
        answer.append(tmp)
    return answer