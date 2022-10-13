import math
def solution(fees, records):
    D = {}
    C = {}

    for i in records:
        t, n, r = i.split()
        h, m = map(int, t.split(':'))

        if n not in D:
            D[n] = h * 60 + m

        else:
            if n not in C:
                C[n] = h * 60 + m - D[n]
            else:
                C[n] += h * 60 + m - D[n]
            del(D[n])

    for i in D:
        if i not in C:
            C[i] = 23 * 60 + 59 - D[i]
        else:
            C[i] += 23 * 60 + 59 - D[i]

    answer = []
    arr = sorted(C.keys())
    for i in arr:
        if C[i] <= fees[0]: # 기본 시간 이하
            answer.append(fees[1])
        else: # 기본 시간 초과
            answer.append(fees[1] + math.ceil((C[i] - fees[0])/fees[2]) * fees[3])

    return answer
