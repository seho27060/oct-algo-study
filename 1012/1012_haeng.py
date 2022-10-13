import math


def solution(fees, records):
    answer = []
    car = {}
    cost = {}

    for i in records:
        A = i.split(' ')
        if A[2] == 'OUT' and A[1] in car:
            now = list(map(int, A[0].split(':')))
            if now[0] == car[A[1]][0]:
                M = now[1] - car[A[1]][1]
            else:
                M = (60 - car[A[1]][1]) + now[1] + (now[0] - (car[A[1]][0] + 1)) * 60

            if A[1] in cost:
                cost[A[1]] += M
            else:
                cost[A[1]] = M
            car.pop(A[1])
        elif A[2] == 'IN':
            car[A[1]] = list(map(int, A[0].split(':')))

            
    for i in car:
        M = (23 - car[i][0]) * 60 + 59 - car[i][1]
        if i in cost:
            cost[i] += M
        else:
            cost[i] = M
    D = sorted(cost.keys())
    for i in D:
        if cost[i] > fees[0]:
            R = fees[1] + math.ceil((cost[i] - fees[0]) / fees[2]) * fees[3]
        else:
            R = fees[1]

        answer.append(R)

    return answer