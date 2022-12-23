def solution(new_id):
    answer = ""
    for c in new_id.lower():
        if c in "abcdefghijklmnopqrstuvwxyz0123456789._-":
            answer += c
    while ".." in answer:
        answer = answer.replace("..",".")
    answer += "a"*(len(answer)==0)
    answer = (answer[0]*(answer[0] != ".") + answer[1:])[0:15]
    answer += "a"*(len(answer)==0)
    answer = answer[0:-1] + answer[-1]*(answer[-1] != ".") 
    while len(answer) < 3:
        answer += answer[-1]
    return answer