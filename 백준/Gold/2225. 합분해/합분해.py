from math import factorial

n, r = map(int, input().split())
print(factorial(n + r - 1) // (factorial(r - 1) * factorial(n)) % 1_000_000_000)