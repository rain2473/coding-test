def solution(order):
    answer, con, new_con = 0, [i for i in range(len(order),0,-1)], []
    while con:
        tmp = con.pop()
        if order[answer] != tmp:
            if new_con and order[answer] == new_con[-1]:
                con.append(tmp)
                new_con.pop()
                answer += 1
            else:
                new_con.append(tmp)
        else:
            answer += 1
    while new_con:
        tmp = new_con.pop()
        if order[answer] != tmp:
            break
        else:
            answer += 1
    return answer