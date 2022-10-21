from heapq import heappop, heappush


def solution(board):
    '''
    N * N
    0 비어 있음, 1 벽
    (0, 0) 출발 (N - 1, N - 1) 도착
    벽이 있는 칸에는 경주로 건설 불가
    직선 도로: 100
    코너: 500 
    -> 즉, 같은 방향이면 100원, 다른 방향이면 100 + 500
    경주로 건설 최소 비용
    => dijkstra
    '''
    N = len(board)
    D = ((1, 0), (-1, 0), (0, 1), (0, -1))
    Q = [(0, 0, 0, -1)]
    visit = set()
    
    while Q:
        curCost, curR, curC, curD = heappop(Q)
        if (curR, curC, curD) in visit: continue
        if (curR, curC) == (N - 1, N - 1): return curCost
        visit.add((curR, curC, curD))
        
        for neiD, (dr, dc) in enumerate(D):
            neiR, neiC = curR + dr, curC + dc
            if 0 <= neiR < N and 0 <= neiC < N and not board[neiR][neiC] and \
                (neiR, neiC, neiD) not in visit:
                if curD == -1 or curD == neiD:
                    heappush(Q, (curCost + 100, neiR, neiC, neiD))
                else:
                    heappush(Q, (curCost + 600, neiR, neiC, neiD))
    
