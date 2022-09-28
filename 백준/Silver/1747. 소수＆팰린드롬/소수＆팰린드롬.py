N = int(input())
        
def det_prime(n):        
    for j in range(2, int(n**0.5)+1):
        if n %j ==0:
            return False
    else:
        return True

for p in range(N, 100030001):
    m = str(p)

    if p == 1:
        continue

    else:
        if m == m[::-1]:
            if det_prime(p) ==True:
                print(p)
                break