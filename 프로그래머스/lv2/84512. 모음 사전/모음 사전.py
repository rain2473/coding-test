from itertools import product
def solution(word):
    answer = set(map(change,product([" ","A","E","I","O","U"],repeat = 5)))
    answer = sorted(list(answer))
    answer = answer.index(word)
    return answer

def change(tup):
    tup = "".join(tup)
    tup = tup.replace(" ","")
    return tup