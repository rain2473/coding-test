def solution(babbling):
    answer = []
    for word in babbling:
        for bab in ["aya", "ye", "woo", "ma"]:
            word = word.replace(bab,".")
        if list(set(list(word))) == ['.']:
            answer.append(word)
    return len(answer)