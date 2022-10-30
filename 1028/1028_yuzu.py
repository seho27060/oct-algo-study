import collections
import math


def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    dic = collections.defaultdict(list)
    for i in range(len(enroll)):
        dic[enroll[i]] = [referral[i], i]

    for j in range(len(seller)):
        ref, idx = dic[seller[j]]
        p = math.floor(amount[j] * 100 * 0.1)
        answer[idx] += (amount[j] * 100) - p

        while ref != "-" and p != 0:
            q = p
            ref, idx = dic[ref]
            p = math.floor(q * 0.1)
            answer[idx] += q - p

    return answer