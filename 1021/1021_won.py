from collections import deque

def f(cd, nd, cost):
    if (cd == 'R' or cd == 'L') and (nd == 'L' or nd == 'R'):
        return cost + 100
    if (cd == 'D' or cd == 'U') and (nd == 'D' or nd == 'U'):
        return cost + 100
    if (cd == 'R' or cd == 'L') and (nd == 'D' or nd == 'U'):
        return cost + 600
    if (cd == 'D' or cd == 'U') and (nd == 'R' or nd == 'L'):
        return cost + 600

def bfs(sr, sc, cost, sd):
    qu = deque()
    visited = [[0] * N for _ in range(N)]
    qu.append([sr, sc, cost, sd])
    visited[sr][sc] = 0
    while qu:
        cr, cc, cur_cost, cd = qu.popleft()

        if cr == N - 1 and cc == N - 1:
            ans.append(cur_cost)
            continue

        for dr, dc, nd in ((-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == 0:
                new_cost = f(cd, nd, visited[cr][cc])
                if visited[nr][nc] == 0 or visited[nr][nc] > new_cost:
                    visited[nr][nc] = new_cost
                    qu.append([nr, nc, new_cost, nd])

def solution(board):
    global N, G, ans
    ans = []
    N = len(board)
    G = [board[i][:] for i in range(N)]
    bfs(0, 0, 0, 'R')
    bfs(0, 0, 0, 'D')
    return min(ans)