from itertools import permutations
from collections import deque


def solution(expression):
    answer = 0
    number = ''
    op = set()
    q = deque([])
    for i in expression:
        if i.isdigit():
            number += i
        else:
            q.append(number)
            q.append(i)
            op.add(i)
            number = ''
    q.append(number)

    len_op = len(op)
    op = list(op)

    for case in permutations(op, len_op):
        new_q = deque([])
        qq = q.copy()
        for i in range(len_op):

            while qq:
                curr = qq.popleft()

                if curr == case[i]:
                    before = new_q.pop()
                    after = qq.popleft()
                    value = str(eval(before + case[i] + after))
                    new_q.append(value)
                else:
                    new_q.append(curr)

            if len(new_q) == 1:
                answer = max(answer, abs(int(new_q[-1])))
                break
            qq = new_q.copy()
            new_q = deque([])

    return answer