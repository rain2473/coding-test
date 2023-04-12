from collections import deque
def solution(players, callings):
    players_hash = {}
    rank_hash = {}
    callings = deque(callings)
    for i, player in enumerate(players):
        players_hash[player] = i
        rank_hash[i] = player
    while callings:
        tmp = callings.popleft()
        chased = rank_hash[players_hash[tmp] - 1]
        players_hash[tmp] -= 1
        players_hash[chased] += 1
        rank_hash[players_hash[tmp]] = tmp
        rank_hash[players_hash[chased]] = chased
    return list(rank_hash.values())