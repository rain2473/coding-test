def solution(numbers, target):
    answer = [0]
    for n in numbers:
        tmp = []
        while answer:
            a = answer.pop()
            tmp.append(a+n)
            tmp.append(a-n)
        answer = tmp
    return answer.count(target)