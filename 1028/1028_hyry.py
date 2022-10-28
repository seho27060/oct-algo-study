def payToUpper(empNo, connection, earnedMoney, emp, money):
    while emp != "center" and money >= 1:
        underNo = empNo[emp]
        upper = connection[underNo]
        moneyToGive = int(money * 0.1)
        moneyToHave = money - moneyToGive
        if moneyToHave < 1: break
        earnedMoney[underNo] += moneyToHave
        money = moneyToGive
        emp = upper
        

def solution(enroll, referral, seller, amount):
    N = len(enroll)
    M = len(seller)
    
    empNo = {
        "center": 0,
    }
    
    # index (아래 사람) -> val (윗 사람)
    connection = [""] * (N + 1)
    
    for idx in range(N):
        # enroll 번호에 따라 idx 기록
        under = enroll[idx]
        upper = referral[idx]
        if upper == "-": upper = "center"
        empNo[under] = idx + 1
        connection[idx + 1] = upper
    
    earnedMoney = [0] * (N + 1)
    
    for idx in range(M):
        under = seller[idx]
        money = amount[idx] * 100
        payToUpper(empNo, connection, earnedMoney, under, money)
    
    answer = earnedMoney[1:]
    return answer
