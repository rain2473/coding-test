def solution(n, words):
    answer, history = [-1,-1], []
    for i, word in enumerate(words):
        switch = 0
        try:
            check = history[-1][-1]
        except:
            history.append(word)
            switch = 1
            continue
        if check == word[0]:
                if history.count(word) == 0:
                    history.append(word)
                    switch = 1
        if switch != 1:
            answer = [(i+1)%n+((i+1)%n==0)*n,(i+1)//n+((i+1)%n!=0)]
            break
    if answer == [-1,-1]:
        answer = [0,0]
    return answer