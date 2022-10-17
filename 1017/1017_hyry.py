import re


def parseOperator(operator, a, b):  # string, int, int -> int
    if operator not in ('+', '*', '-'):
        raise Exception('wrong operator')
    if operator == '+':
        return a + b
    if operator == '*':
        return a * b
    if operator == '-':
        return a - b


def calculate(lst, operator):
    N = len(lst)
    
    res = []
    idx = 0
    while idx < N:
        if lst[idx] == operator:
            res[-1] = parseOperator(operator, res[-1], int(lst[idx + 1]))
            idx += 1
        else:
            # 100 - 200 * 300 - 500 + 20
            res.append(int(lst[idx]) if isinstance(lst[idx], int) or lst[idx].isdigit() else lst[idx])
        idx += 1
    return res


def calculateAll(lst, firstOperator, secondOperator, thirdOperator):
    firstResult = calculate(lst, firstOperator)
    secondResult = calculate(firstResult, secondOperator)
    thirdResult = calculate(secondResult, thirdOperator)
    return abs(*thirdResult)
    

def solution(expression):
    # + * - 인 경우
    # - + * 인 경우
    # - * + 인 경우
    # * + - 인 경우
    # * - + 인 경우
    
    exp = re.split('([+*-])', expression)
    
    res1 = calculateAll(exp, '+', '-', '*')
    res2 = calculateAll(exp, '+', '*', '-')
    res3 = calculateAll(exp, '-', '*', '+')
    res4 = calculateAll(exp, '*', '+', '-')
    res5 = calculateAll(exp, '-', '+', '*')
    res6 = calculateAll(exp, '*', '-', '+')
    
    answer = max(res1, res2, res3, res4, res5, res6)
    return answer
