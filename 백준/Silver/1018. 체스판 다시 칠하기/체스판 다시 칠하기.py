a, b = map(int, input().split())  # 줄, 길이
chess = ['WBWBWBWB','BWBWBWBW']*4
table = []
ans = []
cut=[]

for _ in range(a):
    table.append(input())
for i in range(a-7):
    tmp = table[i:i+8]
    for j in range(b-7):
        temp = []
        for _ in range(8):
            temp.append(tmp[_][j:j+8])
        cut.append(temp)
for _ in range(len(cut))   :
    tmp = cut[_]
    cnt1 = 0
    cnt2 = 0 
    for k in range(8):         
        for l in range(8):
            if tmp[k][l] != chess[k][l]:
                cnt1 += 1
            else:
                cnt2 += 1
    result = min(cnt1,cnt2)
    ans.append(result)
ans = min(ans)
print(ans)
