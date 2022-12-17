def solution(balls, share):
    x,y = 1,1
    for i in range(balls-share):
        x *= (balls-i)
        y *= (i+1)
    return x//y