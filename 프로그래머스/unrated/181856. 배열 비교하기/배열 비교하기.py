def solution(arr1, arr2):
    return (sum(arr1) != sum(arr2)) * ((sum(arr1) > sum(arr2)) - 0.5) * 2