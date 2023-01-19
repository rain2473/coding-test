def solution(elements):
    max_sum, len_ori = sum(elements), len(elements)
    answer, elements = set([max_sum]), elements * 2
    for i in range(len_ori//2-1,len_ori):
        for j in range(len_ori+1):
            tmp = sum(elements[j:j+i+1])
            if tmp not in answer:
                answer.add(tmp)
                answer.add(max_sum-tmp)
    return len(answer)