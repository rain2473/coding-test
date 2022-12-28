def solution(s):
    zero, count = 0, 0
    while True:
        zero += s.count("0")
        s = str(bin(s.count("1")))[2:]
        count += 1
        if s == "1":
            break
    return [count,zero]