from collections import deque
def solution(cards1, cards2, goal):
    cards1, cards2, goal = cards1[::-1], cards2[::-1], deque(goal)
    answer = "Yes"
    while goal:
        want = goal.popleft()
        try:
            if want == cards1[-1]:
                cards1.pop()
                continue
        except:
            pass
        try:
            if want == cards2[-1]:
                cards2.pop()
                continue
        except:
            pass
        answer = "No"
        break
    return answer