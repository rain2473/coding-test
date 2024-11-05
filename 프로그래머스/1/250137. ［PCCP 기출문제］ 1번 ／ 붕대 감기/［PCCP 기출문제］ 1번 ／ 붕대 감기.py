def solution(bandage, health, attacks):
    attack_idx = 0
    bandage_idx = 0
    now_health = health
    
    for i in range(1, attacks[-1][0] + 1):
        tmp = -1
        if attacks[attack_idx][0] == i:
            tmp = 0
            now_health -= attacks[attack_idx][1]
            attack_idx += 1
            bandage_idx = 0
            if now_health <= 0:
                now_health = -1
                break
        else:
            tmp = 1
            now_health += bandage[1]
            bandage_idx += 1
            if bandage_idx == bandage[0]:
                now_health += bandage[2]
                bandage_idx = 0
            now_health = min(now_health, health)
        
    return now_health