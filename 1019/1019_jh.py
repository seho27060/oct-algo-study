from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1sum = sum(q1)
    q2sum = sum(q2)
    len_q = len(q1)*3

    for i in range(len_q):
        if q1sum == q2sum:
            return answer
        elif q1sum > q2sum:
            tmp = q1.popleft()
            q1sum -= tmp
            q2sum += tmp
            q2.append(tmp)
        elif q1sum < q2sum:
            tmp = q2.popleft()
            q1sum += tmp
            q2sum -= tmp
            q1.append(tmp)
        answer += 1

    return -1