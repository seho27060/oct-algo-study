'''
과거에도 못 풀겠고 지금도 못 풀겠고
N 시간 붙잡고 있어봤지만 시초를 못 잡겠음
내일 서울로 외근 나가야 돼서 일단 커밋
추후 수정해보겠음...
'''

import sys
INF = sys.maxsize

def solution(queue1, queue2):
    answer = INF
    L = len(queue1)
    x, y = sum(queue1), sum(queue2)
    mrg = list(queue1 + queue2)
    p1, p2 = 0, L-1
    cnt = 0
    for p1 in range(2*L):
        if answer < cnt:
            break
        nx, ny, temp = x, y, cnt
        for p2 in range(L, 2*L): 
            
            if answer < temp:
                break
                
            if nx == ny:
                answer = min(answer, temp)
                break
                
            temp += 1
            nx = nx + mrg[p2%(2*L)]
            ny = ny - mrg[p2%(2*L)] 
            
        x = x - mrg[p1]
        y = y + mrg[p1]
        cnt += 1
        
        if x == y:
            answer = min(answer, cnt)
            break
        
    if answer == INF:
        answer = -1
    return answer