def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = str.split(video_len, ':')
    video_len = int(video_len[0]) * 60 + int(video_len[1])
    pos = str.split(pos, ':')
    pos = int(pos[0]) * 60 + int(pos[1])
    op_start = str.split(op_start, ':')
    op_start = int(op_start[0]) * 60 + int(op_start[1])
    op_end = str.split(op_end, ':')
    op_end = int(op_end[0]) * 60 + int(op_end[1])
    if op_start <= pos <= op_end:
            pos = op_end
    for command in commands:
        pos = (command == "prev") * max(0, pos - 10) + (command == "next") * min(video_len, pos + 10)
        if op_start <= pos <= op_end:
            pos = op_end
    return str(pos//60).zfill(2) + ':' + str(pos%60).zfill(2)