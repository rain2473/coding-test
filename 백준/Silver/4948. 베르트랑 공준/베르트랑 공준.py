decimal =[]
for n in range(1, 123456*2):
    if n ==1:
        continue
    for j in range(2, int(n**0.5)+1):
        if n %j ==0:
            break
    else:
        decimal.append(n)
M =1
ans = []

while True:
    M = int(input())
    if M == 0:
        break
    else:
        ans.append(M)

for M in ans:
    tmp =[]
    for i in range(len(decimal)):
        if M <decimal[i] and decimal[i]<= 2*M:
            tmp.append(i)
    print(len(tmp))