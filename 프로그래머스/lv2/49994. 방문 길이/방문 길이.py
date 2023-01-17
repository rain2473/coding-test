def solution(dirs):
    answer, position, visited = 0, [0,0], set("")
    for d in dirs:
        root = [",".join(map(str,position))]
        if d=="U" and position[1] != 5:
            position[1] += 1
        elif d=="D" and position[1] != -5:
            position[1] -= 1
        elif d=="L" and position[0] != -5:
            position[0] -= 1
        elif d=="R" and position[0] != 5:
            position[0] += 1
        else:
            continue
        root += [",".join(map(str,position))]
        if len(list(set(root))) == 2:
            root = "<->".join(sorted(root))
        else:
            root = ""
        if root not in visited:
            visited.add(root)
            answer += 1
    return answer