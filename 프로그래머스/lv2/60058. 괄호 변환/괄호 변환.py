def right(p):
    while True:
        tmp = p.replace("()","")
        if tmp != p:
            p = tmp
        else:
            break
    if p == "":
        return True
    else:
        return False
    
def balance(p):
    answer, check, idx = '', 0, 0
    if p == "":
        return p
    while True:
        if p[idx] == "(":
            check += 1
        else:
            check -= 1
        if check == 0:
            break
        idx += 1
    u, v = p[:idx+1], p[idx+1:]
    if right(u) == True:
        return u + balance(v)
    else:
        answer = "(" + balance(v) + ")"
        u = u[1:-1].replace("(","t")
        u = u.replace(")","(")
        u = u.replace("t",")")
        answer += u
        return answer
        
def solution(p):
    answer = balance(p)
    return answer



