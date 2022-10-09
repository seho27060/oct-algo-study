def solution(gems):
    ansLeft = ansRight = 1
    
    gemCnt = len(gems)
    # 먼저 중복되지 않는 보석들의 수 구하기
    gemSet = set(gems)
    gemSetCnt = len(gemSet)
    if gemSetCnt == 1: return [ansLeft, ansRight]
    
    # two pointers?
    left = 0
    gemDic = dict()
    gemDic[gems[left]] = 1
    minLen = 1e10
    for right in range(1, gemCnt):
        gemDic[gems[right]] = gemDic.get(gems[right], 0) + 1
        if len(gemDic) == gemSetCnt and minLen > right - left:
            minLen = right - left
            ansLeft, ansRight = left, right
        while gemDic[gems[left]] >= 2:
            gemDic[gems[left]] -= 1
            left += 1
            if len(gemDic) == gemSetCnt and minLen > right - left:
                minLen = right - left
                ansLeft, ansRight = left, right
        
    return [ansLeft + 1, ansRight + 1]
    