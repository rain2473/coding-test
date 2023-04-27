def solution(arr, n):
    return [arr[i] + n * (i % 2 != len(arr) % 2) for i in range(len(arr))]