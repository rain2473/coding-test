def solution(participant, completion):
    dict_par = {}
    tmp = 0
    for person in participant:
        dict_par[hash(person)] = person
        tmp += int(hash(person))
    for person in completion:
        tmp -= hash(person)
    return dict_par[tmp]