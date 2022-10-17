import re
import copy

def solution(expression):
    global answer
    answer = 0
    expression = re.split('([-|+|*])', expression)

    def solve(q1, x, y, z):
        global answer
        q2 = []
        while q1:
            t = q1.pop(0)
            if t == x:
                q2.append(str(eval(q2.pop() + t + q1.pop(0))))
            else:
                q2.append(t)

        q3 = []
        while q2:
            t = q2.pop(0)
            if t == y:
                q3.append(str(eval(q3.pop() + t + q2.pop(0))))
            else:
                q3.append(t)

        ans = []
        while q3:
            t = q3.pop(0)
            if t == z:
                ans.append(str(eval(ans.pop() + t + q3.pop(0))))
            else:
                ans.append(t)

        answer = max(answer, abs(eval(''.join(ans))))
        return

    q1 = copy.deepcopy(expression)
    solve(q1, '-', '+', '*')
    q1 = copy.deepcopy(expression)
    solve(q1, '-', '*', '+')
    q1 = copy.deepcopy(expression)
    solve(q1, '+', '-', '*')
    q1 = copy.deepcopy(expression)
    solve(q1, '+', '*', '-')
    q1 = copy.deepcopy(expression)
    solve(q1, '*', '+', '-')
    q1 = copy.deepcopy(expression)
    solve(q1, '*', '-', '+')

    return answer