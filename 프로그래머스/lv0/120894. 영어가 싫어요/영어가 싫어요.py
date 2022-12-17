def solution(numbers):
    english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in english:
        numbers = numbers.replace(word,str(english.index(word)))
    return int(numbers)