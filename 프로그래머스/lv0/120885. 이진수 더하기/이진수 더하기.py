def solution(bin1, bin2):
    answer = ""
    tmp = 0
    for i in str(int(bin1) + int(bin2))[::-1]:
        answer += str(int(i) + tmp - 2 * (int(i) + tmp >= 2))
        tmp = (int(i) + tmp >= 2)*1
    return str(tmp)*(tmp == 1) + answer[::-1]