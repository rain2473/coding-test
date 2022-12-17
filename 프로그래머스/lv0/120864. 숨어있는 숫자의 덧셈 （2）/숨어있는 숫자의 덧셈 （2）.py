def solution(my_string):
    answer, tmp = [], ""
    for n in my_string:
        try:
            tmp += str(int(n))
        except:
            try:
                answer.append(int(tmp))
                tmp = ""
            except:
                continue
    try:
        return sum(answer) + int(tmp)
    except:
        return sum(answer)