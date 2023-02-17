from collections import Counter
def solution(topping):
    answer, big, small = 0, Counter(topping), set()
    while len(topping) > 1:
        tmp = topping.pop()
        small.add(tmp)
        if big[tmp] > 1:
            big[tmp] -= 1
        else:
            del big[tmp]
        if len(big) == len(small):
            answer += 1
        elif len(big) < len(small):
            break
    return answer