def hanoi(n,a,b,c):
    if n == 1:
        answer = [[a, c]]
    else:
        answer = hanoi(n-1,a,c,b) + [[a,c]] + hanoi(n-1,b,a,c)
    return answer

n = int(input())
answer = hanoi(n,1,2,3)
print(len(answer))
for a in answer:
    print(a[0], a[1])