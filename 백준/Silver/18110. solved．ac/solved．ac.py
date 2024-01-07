from collections import deque

inputs = []

N = int(input())
outlier = int(N * 0.15 + 0.5)

for i in range(N):
    inputs.append(int(input()))

inputs = deque(sorted(inputs))

for i in range(outlier):
    inputs.pop()
    inputs.popleft()

try:
    print(int(sum(inputs)/len(inputs) + 0.5))
except:
    print(0)