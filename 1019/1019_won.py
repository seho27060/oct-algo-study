def solution(queue1, queue2):
    cnt = 0
    qu = queue1 + queue2
    total = sum(queue1) + sum(queue2)
    if total % 2 == 1:
        return -1
    target = total // 2
    cur = sum(queue1)
    i = 0
    k = len(queue1) - 1
    while i < len(qu) and k < len(qu):
        if cur == target:
            return cnt
        elif cur < target and k < len(qu) - 1:
            k += 1
            cur += qu[k]
        else:
            cur -= qu[i]
            i += 1
        cnt += 1
    return -1