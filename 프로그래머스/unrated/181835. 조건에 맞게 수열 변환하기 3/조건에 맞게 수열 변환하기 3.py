def solution(arr, k):
    answer = [(k + i) * (k % 2 == 0) + (k * i) * (k % 2 != 0) for i in arr]
    return answer