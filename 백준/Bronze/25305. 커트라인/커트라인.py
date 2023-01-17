a, b = map(int,input().split(" "))
t = sorted(list(map(int,input().split(" "))), reverse = True)
print(t[b-1])