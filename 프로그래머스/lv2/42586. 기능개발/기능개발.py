from collections import deque
def solution(progresses, speeds):
    progresses, speeds, answer,finished = deque(progresses), deque(speeds), [], 1
    progress, speed = progresses.popleft(), speeds.popleft()
    day = (100-progress)//speed + ((100-progress)%speed!=0)
    while progresses:
        progress, speed = progresses.popleft(), speeds.popleft()
        if progress + speed * day >= 100:
            finished += 1
        else:
            answer.append(finished)
            day = (100-progress)//speed + ((100-progress)%speed!=0)
            finished = 1
    answer.append(finished)
        
    return answer