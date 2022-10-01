def selfnumber(x):
    y = 0
    z = list(str(x))
    for i in range(len(z)):
        y += int(z[i])
    y += x
    return y

tmp =[]
num = set(range(1,10001))

for i in range(1,10001):
    tmp.append(selfnumber(i))
tmp = set(tmp)
tmp = sorted(num - tmp)
for i in tmp:
    print(i)