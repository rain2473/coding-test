def solution(n, stations, w):
    answer, end, wide = 0, 0, 2 * w + 1
    for station in stations:
        if station - w <= 1:
            start = 1
        else:
            start = station - w
            answer += (start-end-1) // wide + ((start-end-1) % wide != 0)
        if station + w >= n:
            end = n
        else:
            end = station + w
    if end < n:
        answer += (n-end) // wide + ((n-end) % wide != 0)
    return answer