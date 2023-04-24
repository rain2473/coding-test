a = int(input())
det = 'even' * (a % 2 == 0) + 'odd' * (a % 2 != 0)
print(str(a) + " is " + det)