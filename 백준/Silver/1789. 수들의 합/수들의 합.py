s = int(input())
i = 0
x = 0

while x < s:
    i += 1
    x = i*(i+1)//2
if x == s:
    print(i)
else:
    print(i-1)