from itertools import combinations
def solution(numbers):
    return sorted(list(set(map(sum,list(combinations(numbers,2))))))