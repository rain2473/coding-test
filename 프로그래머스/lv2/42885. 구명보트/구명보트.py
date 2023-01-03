from collections import deque
def solution(people, limit):
    people, answer = deque(sorted(people, reverse =True)), 0
    while len(people) != 0:
        tmp = people.popleft()
        try:
            if tmp + people[-1] <= limit:
                people.pop()
        except:
            pass
        answer += 1
    return answer