def solution(expression):
    answer = 0
    expression = str.replace(expression, '*', ',*,')
    expression = str.replace(expression, '+', ',+,')
    expression = str.replace(expression, '-', ',-,')
    expression = expression.split(',')
    
    answer = max(answer, solveAuto(['*', '+', '-'], expression))
    answer = max(answer, solveAuto(['*', '-', '+'], expression))
    answer = max(answer, solveAuto(['+', '*', '-'], expression))
    answer = max(answer, solveAuto(['+', '-', '*'], expression))
    answer = max(answer, solveAuto(['-', '*', '+'], expression))
    answer = max(answer, solveAuto(['-', '+', '*'], expression))
    
    return answer

def solveAuto(operator, sample):
    first = solveCalculation(operator[0], sample)
    second = solveCalculation(operator[1], first)
    last =  solveCalculation(operator[2], second)
    return abs(last[0])
    
def solveCalculation(operator, sample):
    skip = 0
    calc = 0
    result = []
    for i, word in enumerate(sample):
        if skip != 0:
            skip = 0
            continue
        if word != operator:
            result.append(word)
            continue
        prev = result.pop()
        if operator == '*':
            calc = int(prev) * int(sample[i + 1])
        elif operator == '+':
            calc = int(prev) + int(sample[i + 1])
        elif operator == '-':
            calc = int(prev) - int(sample[i + 1])
        result.append(calc)
        skip = 1
    return result