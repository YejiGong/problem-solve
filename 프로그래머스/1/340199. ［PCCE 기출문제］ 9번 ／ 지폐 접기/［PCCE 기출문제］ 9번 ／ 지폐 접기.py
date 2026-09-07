def solution(wallet, bill):
    answer = 0
    wallet_w, wallet_h = wallet
    w, h = bill
    while True:
        if min(w,h) <= min(wallet_w, wallet_h) and max(w,h) <= max(wallet_w, wallet_h):
            break
        else:
            answer += 1
            if w > h:
                w = w//2
            else:
                h = h//2
    return answer