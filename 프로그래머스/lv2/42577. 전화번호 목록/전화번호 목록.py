def solution(phone_book):
    answer, phone_book = True, sorted(phone_book)
    for i,num in enumerate(phone_book):
        try:
            if len(num) >= len(phone_book[i+1]):
                continue
            if num == phone_book[i+1][:len(num)]:
                    answer = False
                    break
        except:
            break
    return answer