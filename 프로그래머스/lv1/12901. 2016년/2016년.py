def solution(a, b):
    month = {1:0,2:31,3:60,4:91,5:121,6:152,7:182,8:213,9:244,10:274,11:305,12:335}
    DoW = "SUN,MON,TUE,WED,THU,FRI,SAT".split(",")
    return DoW[(month[a] + b + 4) % 7]