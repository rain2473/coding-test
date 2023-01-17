n = int(input())
answer = [0]+[1]*(n+1)
for i in range(2,n+1):
    answer[i] = answer[i-1] + answer[i-2]
print(answer[n])