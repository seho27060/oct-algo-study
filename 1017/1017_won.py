import re
from itertools import permutations

def cal(op, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if op == '-':
        return num1 - num2
    if op == '+':
        return num1 + num2
    if op == '*':
        return num1 * num2

def solution(expression):
    answer = 0
    arr = re.split('([-|+|*])', expression)
    kind = list(permutations(['-', '+', '*'], 3))
    for k in range(6):
        tmp = arr[:]
        for o in range(3):
            i = 0
            while i < len(tmp):
                if tmp[i] == kind[k][o]:
                    res = cal(kind[k][o], tmp[i - 1], tmp[i + 1])
                    tmp[i - 1] = res
                    del tmp[i]
                    del tmp[i]
                    i -= 1
                i += 1
        tmp = abs(tmp[0])
        answer = max(answer, tmp)
    return answer