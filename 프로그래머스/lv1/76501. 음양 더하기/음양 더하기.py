def solution(absolutes, signs):
    return sum([absolutes[i]*((s == True)*2-1) for i,s in enumerate(signs)])