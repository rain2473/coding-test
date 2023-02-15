def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for sk in skip:
        alphabet = alphabet.replace(sk,"") 
    answer = ''
    for c in s:
        tmp = alphabet.index(c)+index
        new = alphabet[tmp % len(alphabet)]
        answer += new
    return answer