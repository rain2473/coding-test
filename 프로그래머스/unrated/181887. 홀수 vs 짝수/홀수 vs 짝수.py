def solution(num_list):
    even = 0
    odd = 0
    for i,n in enumerate(num_list):
        if i % 2 == 0:
            odd += n
        else:
            even += n
    return max(odd,even)