def solution(array, n):
    answer = []
    for i in array:
        try:
            answer.append([abs(i-n),abs(i-n)//(i-n)])
        except:
            return n
    answer = sorted(answer)
    return answer[0][0]*answer[0][1]+n