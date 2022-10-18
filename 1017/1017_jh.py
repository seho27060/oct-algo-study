from itertools import permutations

def calc(expression, operator):
    lst = []
    tmp = ""
    for i in expression:
        #숫자 문자 구분
        if i.isdigit() == True:
            tmp += i
        else:
            lst.append(tmp)
            lst.append(i)
            tmp = ""
    lst.append(tmp)

    for i in operator:
        lst2 = []
        while len(lst) != 0:
            tmp = lst.pop(0)
            if tmp == i:
                if i == '+':
                    lst2.append(str(int(lst2.pop()) + int(lst.pop(0))))
                if i == '-':
                    lst2.append(str(int(lst2.pop()) - int(lst.pop(0))))
                if i == '*':
                    lst2.append(str(int(lst2.pop()) * int(lst.pop(0))))
            else:
                lst2.append(tmp)
        lst = lst2

    return abs(int(lst[0]))

def solution(expression):
    operator = ['+','-','*']
    operator = list(permutations(operator, 3))
    answer = []

    for i in operator:
        answer.append(calc(expression, i))

    return max(answer)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))