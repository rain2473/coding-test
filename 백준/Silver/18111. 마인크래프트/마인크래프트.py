M, N, B = map(int,input().split(" "))
height, answer = {}, 150000000
for m in range(M):
    row = list(map(int,input().split(" ")))
    for x in row:
        try:
            height[x] += 1
        except:
            height[x] = 1
for i in range(257):
    big, small = 0, 0
    for k,v in height.items():
        if k == i:
            continue
        elif k < i:
            small += (i-k)*v
        else:
            big += (k-i)*v
    if B + big >= small:
        if small + (big * 2) <= answer:
            answer = small + (big * 2)
            idx = i
print(answer, idx)