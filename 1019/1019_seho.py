# 221020 두 큐 합 같게 만들기
# 두개의 큐, 각 길이는 300,000

# 문제만 곧이 곧대로 받아들이지 말자..

# 처음에는 백트래킹 -> n = 300,000 * 2. 2의 제곱일시..
# 큐라는 자료구조에서 경우의 수는 규칙적

from collections import deque

def solution(queue1, queue2):
    answer = 10e9
    cnt = 0
    q1, q2 = deque(queue1), deque(queue2)
    sumQ1, sumQ2 = sum(q1),sum(q2)

    while cnt <= len(queue1)*2+2:
        if sumQ1 == sumQ2:
            answer = cnt
            break
        # print(q1,q2)
        if sumQ1 < sumQ2 and q2:
            q = q2.popleft()
            sumQ1 += q
            sumQ2 -= q
            q1.append(q)
        elif sumQ1 > sumQ2 and q1:
            q = q1.popleft()
            sumQ1 -= q
            sumQ2 += q
            q2.append(q)
        else:
            return -1
        cnt += 1
        if answer >= 10e9:
            answer = -1
    return answer
