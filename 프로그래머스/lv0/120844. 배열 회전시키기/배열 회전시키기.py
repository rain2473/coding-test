def solution(numbers, direction):
    if direction=="right":
        return [numbers.pop((len(numbers)-1))] + numbers
    else:
        return numbers + [numbers.pop(0)]