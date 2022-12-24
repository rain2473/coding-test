def solution(id_list, report, k):
    report = list(set(report))
    result, answer = {}, []
    for repo in report:
        try:
            result[repo.split(" ")[1]].append(repo.split(" ")[0])
        except:
            result[repo.split(" ")[1]] = [repo.split(" ")[0]]
    for repo in result.values():
        if len(repo) >= k:
            answer += repo
    return [answer.count(id) for id in id_list]