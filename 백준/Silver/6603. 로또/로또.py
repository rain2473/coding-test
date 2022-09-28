from sys import stdin
from itertools import combinations

while 1:
    tmp  = list(map(int, input().split(' ')))
    k = tmp.pop(0)
    
    if k == 0:
        break
        
    else:
        for ans in list(combinations(tmp, 6)):
            ans = list(ans)
            for a in ans:
                print(a, end=' ')
            print()                
        print()