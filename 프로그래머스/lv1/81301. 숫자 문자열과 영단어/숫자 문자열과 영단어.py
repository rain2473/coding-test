def solution(s):
    num = "zero,one,two,three,four,five,six,seven,eight,nine".split(",")
    for n in num:
        s = s.replace(n,str(num.index(n)))
    return int(s)