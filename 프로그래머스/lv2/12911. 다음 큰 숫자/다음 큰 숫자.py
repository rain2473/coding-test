def solution(n):
    result = str(bin(n))[2:].count("1")
    while True:
        n += 1
        count = str(bin(n))[2:].count("1")
        if count == result:
            break
    return n