def solution(gems):
    #보석 종류
    type = len(set(gems))
    left = 0
    right = 0
    dicGems = {}
    ans = [1, len(gems)+1]

    while right < len(gems):
        if gems[right] not in dicGems:
            dicGems[gems[right]] = 1  #새로운 보석종류
        else: #중복
            dicGems[gems[right]] += 1

        if len(dicGems) == type:
            while left <= right:
                if dicGems[gems[left]] > 1:
                    dicGems[gems[left]] -= 1
                    left += 1
                else:
                     if right-left < ans[1] - ans[0]: #더 먼저 시작하는 경우
                         ans = [left+1, right+1]
                     break
        right += 1

    return ans

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))