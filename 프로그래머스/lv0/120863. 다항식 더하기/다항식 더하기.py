def solution(polynomial):
    a, b = 0,0
    for n in polynomial.split(" + "):
        try:
            b += int(n)
        except:
            try :
                a += int(n.replace("x",""))
            except:
                a += 1
    return (str(a)*(a!=1)+"x")*(a!=0)+(" + ")*(a*b!=0)+(str(b))*(b!=0)