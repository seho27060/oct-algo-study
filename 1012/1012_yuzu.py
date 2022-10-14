import collections
import math

def solution(fees, records):
    fee0, fee1, fee2, fee3 = fees
    park = collections.defaultdict(int)
    out = collections.defaultdict(int)
    answer = []
    for record in records:
        time, car, history = record.split()
        h, m = time.split(":")
        minute = int(h) * 60 + int(m)

        if history == 'IN':
            park[car] = minute
        else:
            out[car] += minute - park[car]
            del park[car]

    for car, minute in park.items():
        out[car] += 23 * 60 + 59 - minute

    out = sorted(list(out.items()))
    for car, minute in out:
        answer.append(fee1 + math.ceil(max(0, (minute - fee0)) / fee2) * fee3)

    return answer