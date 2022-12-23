def solution(survey, choices):
    answer = {"RT":0,"CF":0,"JM":0,"AN":0}
    ans = ""
    for i,s in enumerate(survey):
        try:
            answer[s] += choices[i]-4
        except:
            rev = s[::-1]
            answer[rev] += 4-choices[i]
    for i,k in enumerate(list(answer.values())):
        ans += (k > 0)*(list(answer.keys())[i][1]) + (k <= 0)*(list(answer.keys())[i][0])
    return ans