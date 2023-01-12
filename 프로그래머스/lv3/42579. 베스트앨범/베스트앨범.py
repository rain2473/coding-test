def solution(genres, plays):
    answer, songs, genre_record = [], {}, {i:0 for i in list(set(genres))}
    for i in range(len(plays)):
        songs[i] = [genres[i],plays[i]]
        genre_record[genres[i]] += plays[i]
    for idx in sorted(genre_record, key = lambda x:genre_record[x],reverse =True):
        tmp = {}
        for song, info in songs.items():
            if info[0] == idx:
                tmp[song] = info[1]
        answer += sorted(tmp, key = lambda x:tmp[x],reverse =True)[:2]
    return answer