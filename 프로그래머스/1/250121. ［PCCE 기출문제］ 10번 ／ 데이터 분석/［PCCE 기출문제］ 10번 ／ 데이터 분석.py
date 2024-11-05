def solution(data, ext, val_ext, sort_by):
    result = []
    answer = {}
    col_key = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    ext = col_key[ext]
    sort_by = col_key[sort_by]
    for row in data:
        if row[ext] < val_ext:
            answer[row[sort_by]] = row
    for key in sorted(answer.keys()):
         result.append(answer[key])
    return result