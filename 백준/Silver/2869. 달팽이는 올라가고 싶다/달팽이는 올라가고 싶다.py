A, B, V = map(int, input().split(' '))
tmp = (V- B)/(A-B)
if tmp % int(tmp) == 0:
    print(int(tmp))
else:
    print(int(tmp)+1)