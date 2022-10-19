# 계산기 구현이 떠오르던 문제
# 연산자가 3개 뿐이라 순서를 직접 정해서 풀이

import re

def solution(expression):
    answer = []
    expression = re.split('([-|+|*])', expression)

    def oper(num1, op, num2):
        if op == "+":
            return num1 + num2
        if op == "-":
            return num1 - num2
        if op == "*":
            return num1 * num2

    def cal(e, o1, o2, o3):
        lst1 = []
        idx = 0
        while idx < len(e):
            if e[idx] == o1:
                lst1.append(oper(lst1.pop(), e[idx], int(e[idx + 1])))
                idx += 1
            elif e[idx] == o2 or e[idx] == o3:
                lst1.append(e[idx])
            else:
                lst1.append(int(e[idx]))
            idx += 1

        lst2 = []
        idx = 0
        while idx < len(lst1):
            if lst1[idx] == o2:
                lst2.append(oper(lst2.pop(), lst1[idx], lst1[idx + 1]))
                idx += 1
            else:
                lst2.append(lst1[idx])
            idx += 1

        ans = lst2[0]
        idx = 1
        while idx < len(lst2):
            ans = oper(ans, lst2[idx], lst2[idx + 1])
            idx += 2
        answer.append(abs(ans))

    cal(expression, "+", "-", "*")
    cal(expression, "+", "*", "-")
    cal(expression, "-", "*", "+")
    cal(expression, "-", "+", "*")
    cal(expression, "*", "+", "-")
    cal(expression, "*", "-", "+")
    return max(answer)

solution("100-200*300-500+20")