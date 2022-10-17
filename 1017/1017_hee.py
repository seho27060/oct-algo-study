from itertools import permutations
from collections import deque

def trans(txt):
    ST = []
    temp = ''
    for i in txt:
        if not i.isdigit():
            ST.append(temp)
            ST.append(i)
            temp = ''
        else:
            temp += i
    ST.append(temp)
    return ST

def calcul(oper, arr):
    ST = deque(arr)
    ans = []
    while ST:
        s = ST.popleft()
        if s == oper:
            num1 = ans.pop()
            num2 = ST.popleft()
            ans.append(str(eval(num1 + s + num2)))
        else:
            ans.append(s)
    return ans

def solution(expression):
    answer = 0
    arr = trans(expression)
    for a, b, c in permutations(['*', '+', '-'], 3):
        first = calcul(a, arr)
        second = calcul(b, first)
        answer = max(answer, abs(eval(''.join(second))))
    return answer