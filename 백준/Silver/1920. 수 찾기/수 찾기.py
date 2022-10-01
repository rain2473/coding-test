import sys
N = int(sys.stdin.readline())
tmp = sorted(list(map(int,sys.stdin.readline().split(' '))))
    
M = int(sys.stdin.readline())
comp = list(map(int,sys.stdin.readline().split(' ')))

def binary_search(sample,target,start,end):
    if start > end:
        return 0
    
    m = (start+end)//2
    
    if sample[m] == target:
        return 1
    elif sample[m] > target:
        return binary_search(sample,target,start,m-1)
    elif sample[m] < target:
        return binary_search(sample,target,m+1,end)
for m in range(M):
    print(binary_search(tmp,comp[m],0,N-1))