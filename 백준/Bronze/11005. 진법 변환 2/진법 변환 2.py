import math

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''

N, B = map(int,input().split(' '))

for i in range(math.floor(math.log10(N) / math.log10(B)), -1, -1):
    answer += alphabet[N // B ** i]
    N = N % B ** i
    
print(answer)
