def solution(num_list):
    a = 0
    for n in num_list:
        if n % 2 == 0:
            a += 1
    return [a,len(num_list)-a]