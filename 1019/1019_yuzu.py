from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    n = len(queue1)
    s1 = sum(queue1)
    s2 = sum(queue2)
    sumV = s1 + s2
    sumV //= 2
    answer = 0
    while s1 != (sumV):
        if not queue1 or not queue2:
            return -1
        if answer > (2*n)+1:
            return -1
        if s2 > s1:
            y = queue2.popleft()
            s2 -= y
            s1 += y
            queue1.append(y)
        else:
            x = queue1.popleft()
            s1 -= x
            s2 += x
            queue2.append(x)
        answer += 1

    return answer