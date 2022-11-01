# 221031 순위 검색
# 언어 * 직군 * 경력 * 음식 * 코테점수 ... + -(조건고려안함)
# 50,000 * 100,000
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

from collections import defaultdict
def solution(info, query):
    answer = []
    candidateDict = defaultdict(list)

    for candidate in info:
        splitCandidate = candidate.split(" ")
        candidateDict[" ".join(splitCandidate[:4])].append(int(splitCandidate[4]))
        # print(candidate)
    for key in candidateDict.keys():
        candidateDict[key].sort()

    for q in query:
        translateQuery = q.replace(" and","").split(" ")
        keyQuerys = set(translateQuery[:4])
        keyQuerys.discard("-")
        valueQuery = int(translateQuery[4])
        # print(q,keyQuerys,valueQuery)
        result = 0
        for keys, values in candidateDict.items():
            check = True
            for keyQuery in keyQuerys:
                if keyQuery not in keys:
                    check = False
                    break
            if check:
                l = len(values)
                getL = l
                start, end = 0, l-1
                while start <= end:
                    mid = (start+end)//2
                    if valueQuery <= values[mid]:
                        getL = mid
                        end = mid-1
                    else:
                        start = mid + 1
                result += l - getL
        answer.append(result)

    return answer

print(solution(info , query))