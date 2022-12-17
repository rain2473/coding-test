def solution(s1, s2):
    return len(s1) - len(set(s1)-set(s2))