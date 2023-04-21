from collections import defaultdict
def solution(my_string):
    answer1 = []
    answer2 = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    hashmap = defaultdict(int)
    for s in my_string:
        hashmap[s] += 1
    for a in alphabet:
        answer1.append(hashmap[a.upper()])
        answer2.append(hashmap[a.lower()])
    return answer1 + answer2