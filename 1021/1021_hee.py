import sys
from heapq import *
INF = sys.maxsize

def solution(board):
    N = len(board)
    D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    G = [[[INF] *  4 for _ in range(N)] for _ in range(N)]
    Q = []

    if board[1][0] == 0:
        G[1][0][3] = 100
        heappush(Q, (100, 0, 1, 3))
        
    if board[0][1] == 0:
        G[0][1][1] = 100
        heappush(Q, (100, 1, 0, 1))
    
    while Q:
        c, x, y, d = heappop(Q)
        
        for i in range(4):
            if d == i:
                tc = c + 100
            else:
                tc = c + 600
            
            nx = x + D[i][0]
            ny = y + D[i][1]
            
            if -1 < nx < N and -1 < ny < N and tc <= G[ny][nx][i] and (not board[ny][nx]):
                G[ny][nx][i] = tc
                heappush(Q, (tc, nx, ny, i))
                
    answer = min(G[N-1][N-1])
    return answer