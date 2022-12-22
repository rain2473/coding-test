def solution(arr):
    arr.pop(arr.index(min(arr)))
    return arr + [-1] * (len(arr)==0)