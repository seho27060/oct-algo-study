from collections import deque

def solution(board):
    N = len(board)
    answer = int(1e9)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    visited = {(0, 0, 0): 0, (0, 0, 1): 0, (0, 0, 2): 0, (0, 0, 3): 0}

    q = deque()
    q.append((0, 0, -1, 0)) # x, y, dir, cost

    while q:
        x, y, dir, cost = q.popleft()

        for d in range(4):
            newx = x + dx[d]
            newy = y + dy[d]
            if 0 <= newx < N and 0 <= newy < N and board[newx][newy] != 1:
                if (dir - d) % 2 == 0 or dir == -1: #평행한 방향
                    newcost = cost + 100
                else:                               # 꺾인 방향
                    newcost = cost + 600

                if (newx, newy) == (N-1, N-1):
                    answer = min(answer, newcost)
                elif visited.get((newx, newy, d)) is None or visited.get((newx, newy, d)) > newcost:
                    visited[(newx, newy, d)] = newcost
                    q.append((newx, newy, d, newcost))

    return answer