N,M = map(int,input().split(" "))
answer, result =[], []
for n in range(N*2):
    answer.append(list(map(int,input().split(" "))))
for n in range(N):
    for m in range(M):
        if m != M-1:
            print(answer[n][m] + answer[n+N][m], end =" ")
        else:
            print(answer[n][m] + answer[n+N][m], end ="\n")