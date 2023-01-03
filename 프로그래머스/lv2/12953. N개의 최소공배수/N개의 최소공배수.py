from math import gcd

def lcm(a,b):
    return a*b //gcd(a,b)

def solution(arr):
    arr = sorted(arr, reverse = True)
    
    while arr:
        tmp = arr.pop()
        try:
            answer = lcm(answer,tmp)
        except:
            answer = tmp
    return answer