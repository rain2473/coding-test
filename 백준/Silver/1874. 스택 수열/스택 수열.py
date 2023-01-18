make, stack, idx, n, answer = [], [], 0, 1, ""
for i in range(int(input())):
    make.append(int(input()))
while idx < len(make):
    stack.append(n)
    answer += "+"
    if make[idx] == n:
        n += 1
        try:
            while make[idx] == stack[-1]:
                stack.pop()
                answer += "-"
                idx += 1
                if len(stack) == 0:
                    break
        except:
            break
    elif make[idx] < stack[-1]:
        answer = ""
        print("NO")
        break
    else:
        n += 1
for s in answer:
    print(s)