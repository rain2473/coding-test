import heapq
def solution(operations):
    answer = []
    for order in operations:
        try:
            if order == "D 1":
                answer.pop()
            elif order == "D -1":
                heapq.heappop(answer)
            else:
                tmp = int(order[2:])
                heapq.heappush(answer,tmp)
        except:
            continue
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0,0]