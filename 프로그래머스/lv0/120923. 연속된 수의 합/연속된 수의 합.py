def solution(num, total):
    return [i-num//2 + int((total / num * 2 + (num % 2 == 0))/2) for i in range(num)]