def solution(s):
    return (len(s)%2==0) * (s[len(s)//2-1]) + s[len(s)//2]