def find(parent, money, num, ans):
    if parent[num] == num or money // 10 == 0:
        ans[num] += money
        return
    send = money // 10
    mine = money - send
    ans[num] += mine
    find(parent, send, parent[num], ans)
    return

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0] * (n + 1)
    dic = {}
    parent = [i for i in range(n + 1)]
    for i in range(n):
        dic[enroll[i]] = i + 1
    for i in range(n):
        if referral[i] == "-":
            parent[i + 1] = 0
        else:
            parent[i + 1] = dic[referral[i]]
    for i in range(len(seller)):
        find(parent, amount[i] * 100, dic[seller[i]], answer)
    return answer[1:]