def solution(my_string):
    return "".join([(c.upper())*(c.upper()!=c) + (c.lower())*(c.lower()!=c) for c in my_string])