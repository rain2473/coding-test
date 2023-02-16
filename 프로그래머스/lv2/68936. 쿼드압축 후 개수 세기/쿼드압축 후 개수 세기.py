def solution(arr):
    if len(arr) == 1:
        result = [[arr[0][0]]]
    else:
        result = quarter(arr)
    if result == [1]*4 or result == [0]*4:
        result = [[sum(result)!=0]]
    answer = list_to_int(result)
    return answer

def quarter(arr):
    a, b, c, d = [], [], [], []
    top, bottom = arr[:len(arr)//2], arr[len(arr)//2:]
    for i in range(len(top)):
        a.append(top[i][:len(top[i])//2])
        b.append(top[i][len(top[i])//2:])
        c.append(bottom[i][:len(top[i])//2])
        d.append(bottom[i][len(top[i])//2:])
    answer = [a, b, c, d]
    for i,k in enumerate(answer):
        if sum(sum(k,[])) == len(k)*len(k[0]):
            answer[i] = 1
        elif sum(sum(k,[])) == 0:
            answer[i] = 0
        else:
            answer[i] = quarter(k)
    return answer

def list_to_int(arr):
    answer = [0,0]
    while arr:
        tmp = arr.pop()
        try:
            if int(tmp) == 1:
                answer[1] += 1
            else:
                answer[0] += 1
        except:
            arr += tmp
    return answer
        