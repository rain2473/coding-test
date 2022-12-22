def solution(s, n):
    answer = ""
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    for c in s:
        try:
            answer += big[big.index(c)+n]*(c in big)
        except:
            try:
                answer += small[small.index(c)+n]*(c in small)
            except:
                answer += " "
    return answer