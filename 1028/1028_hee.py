from collections import defaultdict

def solution(enroll, referral, seller, amount):
    R = defaultdict(list)
    for i in enroll:
        R[i] = 0
        
    G = defaultdict(list)
    for i in range(len(enroll)):
        G[enroll[i]] = referral[i]
        
    for i in range(len(seller)):
        person = seller[i]
        x = amount[i] * 100
        while person != '-' and x:
            temp = int(x * 0.1)
            R[person] += x - temp
            x = temp
            person = G[person]
    
    answer = []
    for i in enroll:
        answer.append(R[i])
    return answer