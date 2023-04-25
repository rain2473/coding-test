def solution(num_list):
    answer = 1
    for i, num in enumerate(num_list):
        answer *= num
    return (answer < sum(num_list) ** 2) * 1