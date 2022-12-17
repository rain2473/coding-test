def solution(babbling):
    answer = []
    for word in babbling:
        for bab in ["aya", "ye", "woo", "ma"]:
            word = word.replace(bab,".")
            word = word.replace("..",".")
        answer.append(word.replace("..","."))
    return answer.count(".")