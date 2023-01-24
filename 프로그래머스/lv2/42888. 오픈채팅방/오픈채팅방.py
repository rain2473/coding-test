def solution(record):
    record = [tmp.split() for tmp in record]
    answer, name_list, id_list = [], {}, set()
    in_out = {'Leave':'나갔','Enter':'들어왔'}
    for i in range(len(record)-1,-1,-1):
        if record[i][0] == "Enter" or record[i][0] == "Change":
            if record[i][1] not in id_list:
                name_list[record[i][1]] = record[i][2]
                id_list.add(record[i][1])
    for rec in record:
        if rec[0] == "Change":
            continue
        answer.append(f"{name_list[rec[1]]}님이 {in_out[rec[0]]}습니다.")
    return answer