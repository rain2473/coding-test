def solution(fees, records):
    answer, record, in_out, result = {}, {}, {}, []
    for re in records:
        [time, num, IO] = re.split(" ")
        h, m = map(int,time.split(":"))
        time = h * 60 + m
        if IO == "IN":
            try:
                record[num] -= time
            except:
                record[num] = -time
            answer[num] = []
            in_out[num] = 1
        else:
            record[num] += time
            del in_out[num]
            answer[num] += [fees[1] + (record[num]>fees[0]) * fees[3]*((record[num]-fees[0]) // fees[2]+((record[num]-fees[0]) % fees[2]!=0))]
    for num in in_out:
        record[num] += 23 * 60 + 59
        answer[num] += [fees[1] + (record[num]>fees[0]) * fees[3]*((record[num]-fees[0]) // fees[2]+((record[num]-fees[0]) % fees[2]!=0))]
    for num in sorted(answer):
        result += answer[num]
    return result