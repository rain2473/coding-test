from sys import stdin
n, k = map(int,stdin.readline().split(' '))
tmp = []
for _ in range(n):
    tmp.append(int(stdin.readline()))

def finder(x):
    temp = [0 for i in range(k+1)]
    for i in range(1,k+1):
        a =[]
        for j in tmp:
            if j <= i and temp[i - j] != -1:
                a.append(temp[i - j])
        if len(a)==0:
            temp[i] = -1
        else:
            temp[i] = min(a) + 1
    
    return(temp[-1])
        
print(finder(k))