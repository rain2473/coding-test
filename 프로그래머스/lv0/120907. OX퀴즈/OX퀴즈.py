def solution(quiz):
    answer = ["X","O"]
    ans = []
    for formula in quiz:
        formula = formula.split(" ")
        if formula[1] == "+":
            a = 1*(int(formula[0]) + int(formula[2]) == int(formula[4]))
        else:
            a = 1*(int(formula[0]) - int(formula[2]) == int(formula[4]))
        ans.append(answer[a])
    return ans
