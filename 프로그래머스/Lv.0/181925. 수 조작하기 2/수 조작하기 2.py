def solution(numLog):
    commend = ""
    keys = {
        1 : 'w',
        -1 : 's',
        10 : 'd',
        -10 : 'a'
    }
    for i in range(len(numLog) - 1):
        commend += keys[numLog[i + 1] - numLog[i]]
    return commend