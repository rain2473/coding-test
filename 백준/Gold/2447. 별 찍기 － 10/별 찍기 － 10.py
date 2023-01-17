import math
def star(N):
    k = int(math.log(N,3))
    if k == 1:
        answer = ['***','* *','***']
    else:
        a = []
        b = []
        for i,row in enumerate(star(N//3)):
            a.append(row*3)
            b.append(row+" "*len(row)+row)
        answer = a+b+a
    return answer
for row in star(int(input())):
    print(row)