def solution(enroll, referral, seller, amount):
    N = len(enroll)
    d = dict()
    profit = dict()

    for i in range(N):
        d[enroll[i]] = referral[i]
        profit[enroll[i]] = 0

    for idx, name in enumerate(seller):
        person = name
        val = amount[idx]*100
        while True:
            if val * 0.1 < 1:
                profit[person] += val
                break
            profit[person] += val - int(val * 0.1)

            if d[person] == "-":
                break
            person = d[person]
            val = int(val*0.1)

    answer = [value for value in profit.values()]
    return answer