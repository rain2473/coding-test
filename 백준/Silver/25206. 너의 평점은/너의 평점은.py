grade = {}
grade["A+"] = 4.5
grade["A0"] = 4.0
grade["B+"] = 3.5
grade["B0"] = 3.0
grade["C+"] = 2.5
grade["C0"] = 2.0
grade["D+"] = 1.5
grade["D0"] = 1.0
grade["F"] = 0.0

total = 0
score = 0

for i in range(20):
    a, b, c = map(str,input().split(' '))
    if c != "P":
        score += grade[c] * float(b)
        total += float(b)
        
print(score / total)
