def solution(cacheSize, cities):
    cache, answer = [], 0
    if cacheSize != 0:
        for city in cities:
            city = city.lower()
            if cache.count(city) != 0:
                answer -= 4
                cache.pop(cache.index(city))
            elif len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5
    else:
        answer = len(cities)*5
        
    return answer