def solution(book_time):
    book_time.sort(key = lambda x:x[0])
    answer, room = 1, {1:0}
    for guest in book_time:
        new, time = 1, int(guest[1].replace(":",""))
        time += 10 + 40 * (time % 100 >= 50)
        for i in room.keys():
            if room[i] <= int(guest[0].replace(":","")):
                room[i], new = time, 0
                break
        if new == 1:
            answer += 1
            room[answer] = time
    return answer