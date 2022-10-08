
def solution(gems):
    size = len(list(set(gems)))
    dic = {gems[0]: 1}
    tmp = [0, len(gems) - 1]
    s, e = 0, 0

    while s < len(gems) and e < len(gems):
        if len(dic) == size:
            if e - s < tmp[1] - tmp[0]:
                tmp = [s, e]
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1

        else:
            e += 1
            if e == len(gems):
                break
            if gems[e] in dic.keys():
                dic[gems[e]] += 1
            else:
                dic[gems[e]] = 1
    return [tmp[0] + 1, tmp[1] + 1]

