def solution(denum1, num1, denum2, num2):
    a,b = denum1 * num2 + denum2  * num1 , num1 *num2
    for i in range(min(a,b),1,-1):
        if a % i == 0 and b % i == 0:
            a = a//i
            b = b//i
    return [a,b]