# 구현하는 알고리즘
# 상납금 올리는건 재귀로 처리
# 분명 이런 로직 처리하는 알고리즘이 있었는데 기억이 안남....


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    link = dict()
    for i in range(len(enroll)):
        link[enroll[i]] = i
    def money(sellerName, sellerAmount):
        if referral[link[sellerName]] != '-':
            if sellerAmount//10 <= 0:
                answer[link[sellerName]] += sellerAmount
            else:
                answer[link[sellerName]] += sellerAmount - (sellerAmount//10)
                money(referral[link[sellerName]], sellerAmount//10)
        else:
            if sellerAmount // 10 <= 0:
                answer[link[sellerName]] += sellerAmount
            else:
                answer[link[sellerName]] += sellerAmount - sellerAmount//10
    for i in range(len(seller)):
        money(seller[i], amount[i]*100)
    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])