from itertools import combinations
from collections import defaultdict

def lower_bound(s, e, arr, target):
    if s >= e:
        return s
    mid = (s + e) // 2
    if arr[mid] >= target:
        return lower_bound(s, mid, arr, target)
    else:
        return lower_bound(mid + 1, e, arr, target)

def solution(infos, query):
    answer = []
    dic = defaultdict(list)
    for info in infos:
        info = info.split()
        cond = info[:-1]
        num = int(info[-1])
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                tmp = cond[:]
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                dic[key].append(num)

    for value in dic.values():
        value.sort()

    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        key = ''.join(q[:-1])
        num = int(q[-1])
        cnt = 0
        if key in dic:
            arr = dic[key]
            idx = lower_bound(0, len(arr), arr, num)
            cnt = len(arr) - idx
        answer.append(cnt)
    return answer