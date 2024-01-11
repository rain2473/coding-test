from collections import deque
import sys
input = sys.stdin.readline

line = deque(input().split("-"))

answer = 0

for i, chunk in enumerate(line):
    if i == 0:
        answer += sum(map(int, chunk.split("+")))
    else:
        answer -= sum(map(int, chunk.split("+")))
print(answer)