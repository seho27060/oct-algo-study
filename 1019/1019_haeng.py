from collections import deque

def solution(queue1, queue2):
    Q1 = sum(queue1)
    Q2 = sum(queue2)
    target = (Q1+Q2)//2
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    while Q1 != target:
        if Q1 > Q2:
            q1 = queue1.popleft()
            queue2.append(q1)
            Q1 -=q1
            Q2 += q1
        else:
            q2 = queue2.popleft()
            queue1.append(q2)
            Q1 += q2
            Q2 -= q2
        answer += 1
        if answer > 300000:
            answer= -1
            break
    return answer