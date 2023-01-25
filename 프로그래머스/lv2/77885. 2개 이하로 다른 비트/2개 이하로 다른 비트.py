def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            for i,b in enumerate(bin(num)[::-1]):
                if b == "0" or b == "b":
                    answer.append(num + 2**(i-1))
                    break
    return answer