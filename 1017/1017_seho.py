# 221018 수식 최대화
# * + - 연산자들의 순차적 우선순위 경우의 수에서
# 계산한 값들 중 절댓값이 가장 큰 값 출력

# expression = "100-200*300-500+20"
expression = "50*6-3*2"

from itertools import permutations
def solution(expression):
    splitExpression = []
    get = ""
    # expression 을 보기좋게 split
    for exp in expression:
        if exp in ["-","*","+"]:
            splitExpression.append(get)
            splitExpression.append(exp)
            get = ""
        else:
            get += exp
    splitExpression.append(get)

    answer = 0
    # split된 expression에서 연산자만 추출
    calcSet = set([ i for i in expression if i in ["-","*","+"]])
    # permutation으로 경우의수 생성
    calcPermu = list(permutations(calcSet,len(calcSet)))
    # 많아봐야 6개인~ 경우의 수대로~
    for calcList in calcPermu:
        result = []
        # 길어봐야 길이가 100보다 작은 splitExpression 대로~
        getExpression = splitExpression.copy()
        for calc in calcList:
            expLoc = 0
            while expLoc < len(getExpression):
                if getExpression[expLoc] == calc:
                    result[-1] = eval(str(result[-1])+calc+str(getExpression[expLoc+1]))
                    expLoc += 2
                else:
                    result.append(getExpression[expLoc])
                    expLoc += 1
            getExpression = result.copy()
        # 계산 후 최대값 갱신
        answer = max(answer,abs(int(result[-1])))
    return answer

print(solution(expression))