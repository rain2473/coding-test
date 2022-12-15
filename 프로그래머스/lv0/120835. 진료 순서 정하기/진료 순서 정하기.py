def solution(emergency):
    answer = [0 for i in emergency]
    for k,i in enumerate(emergency):
        for j in emergency:
            answer[k] += (i<=j)*1
    return answer