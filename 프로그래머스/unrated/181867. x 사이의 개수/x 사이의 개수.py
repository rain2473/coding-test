def solution(myString):
    answer = []
    myString = myString.split("x")
    for string in myString:
        answer.append(len(string))
    return answer