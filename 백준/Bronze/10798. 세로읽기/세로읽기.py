tmp = []
answer = [' '] * 5 * 15
for i in range(5):
    row = list(input())
    for e, data in enumerate(row):
        answer[e * 5 + i] = data
print("".join(answer).replace(' ',''))