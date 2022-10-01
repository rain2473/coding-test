T = int(input())
tmp=[]
피보=[1,1]

for t in range(T):
    tmp.append(int(input()))

for i in range(2, sorted(tmp)[T-1]):
    피보.append(피보[i-2]+피보[i-1])

for t in tmp:
    if t > 1:
        print(피보[t-2], 피보[t-1])
    elif t == 1:
        print(0, 1)
    elif t == 0:
        print(1, 0)