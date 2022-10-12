from collections import defaultdict
import math

def getDiff(hh, mm, ph, pm):
    dh = hh - ph
    if mm >= pm:
        dm = mm - pm
    else:
        dh -= 1
        dm = mm - pm + 60
    return dh * 60 + dm

def solution(fees, records):
    answer = []
    data = {}
    res = defaultdict(lambda: 0)
    for record in records:
        time, num, flag = record.split()
        hh, mm = map(int, time.split(':'))
        if flag == 'IN':
            data[num] = [hh, mm]
        if flag == 'OUT':
            ph, pm = data[num]
            tmp = getDiff(hh, mm, ph, pm)
            res[num] += tmp
            data[num] = 0
    for key in list(data):
        if data[key] != 0:
            ph, pm = data[key]
            tmp = getDiff(23, 59, ph, pm)
            res[key] += tmp
    for key in res:
        tmp = 0
        if res[key] > fees[0]:
            tmp = fees[1] + math.ceil((res[key] - fees[0]) / fees[2]) * fees[3]
        else:
            tmp = fees[1]
        answer.append([key, tmp])
    answer.sort(key=lambda x: x[0])
    ans = []
    for a in answer:
        ans.append(a[1])
    return ans