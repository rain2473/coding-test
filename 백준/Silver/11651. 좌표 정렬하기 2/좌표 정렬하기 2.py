n = int(input())
plane = []
for i in range(n):
    plane.append(list(map(int,input().split(" "))))
plane.sort()
plane.sort(key = lambda x : x[1])
for i in plane:
    print(i[0], i[1])