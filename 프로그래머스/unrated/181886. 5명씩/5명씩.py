def solution(names):
    answer = []
    for i in range(len(names) // 5 + (len(names) % 5 != 0)):
        answer.append(names[i * 5])
    return answer