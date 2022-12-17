def solution(chicken):
    return chicken // 9 - (chicken % 9 == 0 and chicken//9 != 0)