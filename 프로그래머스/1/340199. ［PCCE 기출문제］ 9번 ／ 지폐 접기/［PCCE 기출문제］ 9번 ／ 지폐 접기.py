def solution(wallet, bill):
    answer = 0
    wallet_w = max(wallet)
    wallet_h = min(wallet)
    bill_w = max(bill)
    bill_h = min(bill)
    
    while bill_w > wallet_w or bill_h > wallet_h:
        tmp = [bill_h, bill_w // 2]
        bill_w = max(tmp)
        bill_h = min(tmp)
        
        answer += 1
    return answer