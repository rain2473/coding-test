from collections import deque
def solution(msg):
    dic_idx, answer, msg = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [], deque(msg)
    tmp = msg.popleft()
    while msg:
        temp = tmp + msg[0]
        if temp not in dic_idx:
            answer.append(dic_idx.index(tmp))
            dic_idx.append(temp)
            tmp = msg.popleft()
        else:
            tmp += msg.popleft()
    answer.append(dic_idx.index(tmp))
    return answer