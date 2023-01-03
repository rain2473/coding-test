def solution(s):
    stack = []
    for x in s:
        try:
            if x != stack[-1]:
                stack.append(x)
            else:
                stack.pop()
        except:
            stack.append(x)
    return (len(stack)==0)*1