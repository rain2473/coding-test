from collections import deque
def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])
    plans, undo = deque(plans), []
    now = change(plans.popleft())
    while plans:
        nowTime = now[1]
        next_ = change(plans.popleft())
        now = task(now, next_, answer, undo)
    now = next_
    answer.append(now[0])
    while undo:
        nowTime = now[1]
        next_ = undo.pop()
        now = task(now, next_, answer, undo)
    return answer

def task(now, next_, answer, undo):
    time = next_[1] - now[1] - now[2]
    if time == 0:
        answer.append(now[0])
        now = next_
    elif time > 0:
        answer.append(now[0])
        nowTime = now[1] + now[2]
        try:
            now = undo.pop()
        except:
            now = next_
            return now
        now[1] = nowTime
        now = task(now, next_, answer, undo)
    elif time < 0:
        now[2] = -time
        undo.append(now)
        now = next_
    return now
        
def change(plan):
    plan[1] = int(plan[1].split(":")[0]) * 60 + int(plan[1].split(":")[1])
    plan[2] = int(plan[2])
    return plan