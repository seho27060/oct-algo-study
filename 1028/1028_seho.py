# 221028 다단계 칫솔 판매
# 민호야.. 다단계가 왠말이니..

# n < 10,000
# 각 직원 번호를 i로 두고 연관관계 형성
# 딕셔너리로 관리
# seller에 따라 번돈 합계 해서
# 합계한대로 줄줄이 계산

def solution(enroll, referral, seller, amount):
    answer = [0] * (len(enroll))
    hierarchy = [-1]*(len(enroll))
    refDict = dict()

    for workerIdx in range(len(enroll)):
        refDict[enroll[workerIdx]] = workerIdx
        if referral[workerIdx] != "-":
            hierarchy[workerIdx] = enroll.index(referral[workerIdx])


    for idx in range(len(seller)):
        start, income = refDict[seller[idx]], amount[idx]*100
        netIncome = income
        # print(start,enroll.index(start),income)
        while start > -1 and netIncome > 0:
            tax = netIncome//10
            netIncome -= tax
            answer[start] += netIncome
            # print(netIncome,worker,result)
            start = hierarchy[start]
            netIncome = tax
    return answer
