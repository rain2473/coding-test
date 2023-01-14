from math import log
def solution(n, k):
    answer, x, result = "", int(log(n,k)), 0
    for i in range(x+1):
        answer += str(n//(k**(x-i)))
        n = n%(k**(x-i))
    answer = sorted(answer.split("0"))
    while answer:
        tmp = answer.pop()
        try:
            tmp = int(tmp)
        except:
            continue
        if prime(tmp):
            result += 1
    return result

def prime(number):
    if number==1:
        return False
    for i in range(2, int(number**(0.5))+1):
        if number%i==0:
            return False
    return True
