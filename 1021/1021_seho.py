# 221021 경주로 건설
# 직선(이동) 100, 코너(방향전환) 500 -> 서로 독립
# n = 25*25
# dfs는 14번 안나오는데.. bfs 는 나옴.. 왜?

from collections import deque

def solution(board):
    moves1 = [[0, -1],[0, 1]]  # 좌우
    moves2 = [[-1, 0], [1, 0]]  # 상하
    answer = 10e9
    # 비용, 방향(1 = 좌우, 2 = 상하)
    limit = len(board)
    visited = [[[10e9, 0]] * limit for _ in range(limit)]
    for start in [1,2]:
        visited[0][0] = [0,start]
        queue = deque([[0,0]])

        while queue:
            now = queue.popleft()
            for move in moves1:
                nxtR,nxtC = now[0] + move[0], now[1] + move[1]
                if 0 <= nxtR < limit and 0 <= nxtC < limit:
                    cost = 100
                    if visited[now[0]][now[1]][1] != 1:
                        cost += 500
                    if visited[nxtR][nxtC][0] >= visited[now[0]][now[1]][0] + cost and board[nxtR][nxtC] != 1:
                        visited[nxtR][nxtC] = [visited[now[0]][now[1]][0] + cost,1]
                        queue.append([nxtR, nxtC])
            for move in moves2:
                nxtR,nxtC = now[0] + move[0], now[1] + move[1]
                if 0 <= nxtR < limit and 0 <= nxtC < limit:
                    cost = 100
                    if visited[now[0]][now[1]][1] != 2:
                        cost += 500
                    if visited[nxtR][nxtC][0] >= visited[now[0]][now[1]][0] + cost and board[nxtR][nxtC] != 1:
                        visited[nxtR][nxtC] = [visited[now[0]][now[1]][0] + cost,2]
                        queue.append([nxtR,nxtC])

        answer = min(answer,visited[-1][-1][0])
    return answer
