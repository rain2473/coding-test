from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer, truck, bridge = 0, deque(truck_weights), deque([0]*bridge_length)
    bridge_weight = 0
    while bridge:
        answer += 1
        out = bridge.popleft()
        bridge_weight -= out
        if truck:
            if bridge_weight + truck[0] <= weight:
                new = truck.popleft()
                bridge_weight += new
                bridge.append(new)
            else:
                bridge.append(0)
    return answer