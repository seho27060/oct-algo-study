def solution(gems):
    n = len(gems)
    setGems = set(gems)
    answer = [1, n]
    l, r = 0, 0
    dicGems = {}
    while r < n:
        if gems[r] not in dicGems:
            dicGems[gems[r]] = 1
        else:
            dicGems[gems[r]] += 1
        if len(dicGems) == len(setGems):
            while l <= r:
                if dicGems[gems[l]] > 1:
                    dicGems[gems[l]] -= 1
                    l += 1
                elif answer[1]-answer[0] > r-l:
                    answer = [l+1, r+1]
                    break
                else:
                    break
        r += 1
    return answer