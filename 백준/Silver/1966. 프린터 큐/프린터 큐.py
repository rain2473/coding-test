from collections import deque
def solution(priorities, location):
    answer, priorities, loca = 0, deque(priorities), deque([0 for i in range(len(priorities))])
    loca[location] = 1
    while priorities:
        tmp = priorities.popleft()
        temp = loca.popleft()
        if len(priorities) > 1 and tmp < max(priorities):
            priorities.append(tmp)
            loca.append(temp)
        else:
            answer += 1
            if temp == 1:
                break
    return answer

for n in range(int(input())):
    a,location = map(int,input().split(" "))
    priorities = list(map(int,input().split(" ")))
    answer = solution(priorities, location)
    print(answer)