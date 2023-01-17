def solution(numbers):
    if set(numbers) == {0}:
        return "0"
    else:
        numbers = sorted(list(map(str,numbers)), key = lambda x:x*3, reverse = True)
        return "".join(numbers)