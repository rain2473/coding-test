from sys import stdin
n, k = map(int,stdin.readline().split(' '))
tmp = []
for _ in range(n):
    tmp.append(int(stdin.readline()))

def finder(k):
    temp = [0 for i in range(k+1)]
    temp[0] = 1
    for j in tmp:
        for i in range(j, k+1):
            if i >= j:
                temp[i] += temp[i-j]
    return(temp[-1])
        
print(finder(k))