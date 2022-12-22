def solution(a, b):
    return (max(a,b)-min(a,b))*(a+b+1)//2 +min(a,b)