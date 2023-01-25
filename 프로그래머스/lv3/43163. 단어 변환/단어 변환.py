from collections import deque
def solution(begin, target, words):
    answer, queue, visited = 0, deque([begin]), {w:0 for w in words}
    if target not in words:
        return answer
    while queue:
        word = queue.pop()
        if word == target:
            break
        visited[word] = 1
        answer += 1
        for w in words:
            tmp = 0
            if visited[w] == 0 and w not in queue:
                for i in range(len(word)):
                    if word[i] != w[i]:
                        tmp += 1
                if tmp == 1:
                    queue.append(w)
        print(word,queue)
    return answer