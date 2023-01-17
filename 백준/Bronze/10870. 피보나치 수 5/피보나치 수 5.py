def Fibonacci(n):
    if n < 2:
        return n
    else:
        return Fibonacci(n-2) +Fibonacci(n-1)
answer = Fibonacci(int(input()))
print(answer)