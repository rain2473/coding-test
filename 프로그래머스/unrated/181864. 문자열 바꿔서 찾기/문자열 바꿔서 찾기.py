def solution(myString, pat):
    myString = myString.replace('A','$').replace('B','A').replace('$', 'B')
    return (pat in myString) * 1