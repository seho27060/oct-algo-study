# 221007 보석 쇼핑
# 진열대에서 싹슬이해서 모든 종류 보석을 가질수있는 "하나"의 구간을 찾아라

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

def solution(gems):
    answer = [1, len(gems)]
    jewelrySet = set(gems)
    answerLen = len(jewelrySet)
    # print(jewelrySet)

    jewelryDict = {gems[0]:1,}

    start, end = 0, 0

    while start < len(gems) and end < len(gems):
        if len(jewelryDict) < answerLen:
            end += 1
            if end == len(gems):
                break
            jewelryDict[gems[end]] = jewelryDict.get(gems[end],0) + 1
        else:
            if (end - start + 1 )< (answer[1] - answer[0] + 1):
                answer = [start+1,end+1]
            if jewelryDict[gems[start]] == 1:
                del jewelryDict[gems[start]]
            else:
                jewelryDict[gems[start]] -= 1
            start += 1

    # answer.sort(key=lambda x:x[1]-x[0])
    # print(dp)
    # print(answer)
    return answer

print(solution(gems))