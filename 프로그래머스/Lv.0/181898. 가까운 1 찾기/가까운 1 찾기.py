def solution(arr, idx):
    arr = arr[idx : ]
    answer = -1
    for i, x in enumerate(arr):
        if x == 1:
            answer = idx + i
            break
    return answer