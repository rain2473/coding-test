def solution(keymap, targets):
    answer, alphabet = [], {s:-1 for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    for key in keymap:
        for i,a in enumerate(alphabet.keys()):
            if a not in key:
                continue
            elif alphabet[a] == -1 or alphabet[a] > key.index(a)+1:
                alphabet[a] = key.index(a)+1
    for target in targets:
        ans = 0
        for s in target:
            if alphabet[s] != -1:
                ans += alphabet[s]
            else:
                ans =-1
                break
        answer.append(ans)
    return answer