from collections import deque

def solution(board):
    dx = [0, 1, -1, 0]
    dy = [-1, 0, 0, 1]
    n = len(board)
    arr = [[[1e10] * 4 for _ in range(n)] for _ in range(n)]
    arr[0][0] = [0, 0, 0, 0]

    q = deque()
    q.append((0, 0, -1))
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            if i + d == 3:
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            cost = 100
            if d != -1 and i != d:
                cost += 500
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                if arr[nx][ny][i] > arr[x][y][d] + cost:
                    arr[nx][ny][i] = arr[x][y][d] + cost
                    q.append((nx, ny, i))

    return min(arr[-1][-1])