import math

a, b, p, c, d, q = map(int,input().split(' '))

x = (d * p - b * q) // (a * d - b * c)
y = (a * q - c * p) // (a * d - b * c)
    
print(str(x) + ' ' + str(y))
