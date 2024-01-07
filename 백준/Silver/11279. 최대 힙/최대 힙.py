import sys
import heapq

heap = []
N = int(sys.stdin.readline())

for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        try:
            print(heapq.heappop(heap) * -1)
        except:
            print(0)
    else:
        heapq.heappush(heap, -tmp)