def solution(age):
    return "".join([list("abcdefghij")[i] for i in list(map(int,str(age)))])