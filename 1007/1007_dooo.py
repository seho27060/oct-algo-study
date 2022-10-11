def solution(gems):
    n = len(gems)
    answer = [0, n]
    ju = len(set(gems))
    s = 0
    e = 0
    dic = {gems[s]: 1}
    while s < n and e < n:
        if len(dic) < ju:
            e += 1
            if e == n:
                break
            dic[gems[e]] = dic.get(gems[e], 0) + 1

        else:
            if (e - s + 1) < (answer[1] - answer[0]) + 1:
                answer = [s, e]
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1

    return [answer[0] + 1, answer[1] + 1]