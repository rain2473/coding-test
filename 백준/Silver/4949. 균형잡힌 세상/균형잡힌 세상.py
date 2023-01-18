import re

def balance(text):
    answer = re.sub(r"[a-zA-Z .]", "", text)
    while True:
        tmp = answer
        tmp = tmp.replace("()","")
        tmp = tmp.replace("[]","")
        if tmp != answer:
            answer = tmp
            continue
        else:
            break
    if len(answer) == 0:
        return "yes"
    else:
        return "no"
    
while True:
    text = input()
    if text ==".":
        break
    answer = balance(text)
    print(answer)