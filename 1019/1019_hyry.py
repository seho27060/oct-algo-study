from collections import deque


def prerequisites(lst):
    newDeque = deque()
    sumV = 0
    
    for item in lst:
        sumV += item
        newDeque.append(item)

    return newDeque, sumV
        

def solution(queue1, queue2):
    '''
    greedy: 합이 작은 쪽의 원소를 큰 쪽으로 옮기기
    만약 한 큐가 다 비어도 합이 같아지지 않는다면 그때는 stop
    
    [3, 1], [3, 3]  -> 시초 케이스
    
    # 이래도 대량으로 넘기는 경우 시초 발생
    # append
    '''
    
    q1, sum1 = prerequisites(queue1)
    q2, sum2 = prerequisites(queue2)
    freezedQ1 = q1.copy()
    
    totalSum = sum1 + sum2
    # target = totalSum // 2
    
    if totalSum % 2 != 0:
        return -1
    
    cnt = 0
    while q1 and q2 and (sum1 != sum2):
        if sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        elif sum1 < sum2:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        
        # cnt >= 10 ** 6은 ... 하드 코딩으로 때려 박은 수치
        # 10 ** 5는 다른 케이스가 덜 돌아서 안 된다
        if freezedQ1 == q1 or cnt >= 10 ** 6:
            return -1
        cnt += 1
    
    if sum1 != sum2:
        return -1
    
    return cnt
