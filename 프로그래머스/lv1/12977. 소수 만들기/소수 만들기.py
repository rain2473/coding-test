from itertools import combinations

def solution(nums):
    answer = 0
    for i in [sum(case) for case in list(combinations(nums,3))]:
        switch = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                switch = 1
                break
        if switch == 0:
            answer += 1
    return answer