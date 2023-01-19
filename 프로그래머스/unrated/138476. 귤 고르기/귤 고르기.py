def solution(k, tangerine):
    answer, count = 0, 0
    num_per_size = [[i,0] for i in range(max(tangerine)+1)]
    for t in tangerine:
        num_per_size[t][1] += 1
    num_per_size.sort(key = lambda x : x[1], reverse =True)
    for n in num_per_size:
        count += 1
        answer += n[1]
        if answer >= k:
            break
    return count