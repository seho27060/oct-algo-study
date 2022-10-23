# bfs를 활용해서 풀이한 문제
# 처음에는 2차원 테이블로 해결하고 싶었는데 실패
# 3차원 변경 후 방향에 따라 테이블 4개 만들기 싫어서 2개로 줄여보려다가 또 실패
# 11번 테케가 시초가 너무 나서 백트래킹까지 적용하고 나서야 풀린문제
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def solution(board):
    answer = 0
    L = len(board)
    arr = [[[0] * 4 for _ in range(L)] for _ in range(L)]
    q = deque()
    q.append([0, 0, 0, -1])
    while q:
        cost, y, x, dir = q.popleft()
        if arr[y][x][dir] < cost:
            continue
        if answer and arr[y][x][dir] >= answer:
            continue
        if y == x == L-1:
            if not answer or answer > arr[y][x][dir]:
                answer = arr[y][x][dir]
                continue
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < L and 0 <= nx < L and not board[ny][nx]:
                if dir == -1 or dir == d:
                    if not arr[ny][nx][d] or arr[ny][nx][d] >= cost + 100:
                        arr[ny][nx][d] = cost + 100
                        q.append([cost + 100, ny, nx, d])
                else:
                    if not arr[ny][nx][d] or arr[ny][nx][d] >= cost + 600:
                        arr[ny][nx][d] = cost + 600
                        q.append([cost+600, ny, nx, d])

    return answer
solution([[0,0,0],[0,0,0],[0,0,0]])

# def solution(board):
#     answer = 0
#     L = len(board)
#     arr = [[[0] * 2 for _ in range(L)] for _ in range(L)]
#     arr[0][0][0] = 100
#     q = deque()
#     q.append([0, 0, -1, 0])
#     while q:
#         y, x, dir, chance = q.popleft()
#         if
#         if y == x == L-1:
#             if not answer or answer > arr[y][x][chance]:
#                 answer = arr[y][x][chance]
#                 continue
#         for d in range(4):
#             ny = y + dy[d]
#             nx = x + dx[d]
#             if 0 <= ny < L and 0 <= nx < L and not board[ny][nx]:
#                 if dir == -1 or dir == d:
#                     if not arr[ny][nx][chance] or arr[ny][nx][chance] >= arr[y][x][chance] + 100:
#                         arr[ny][nx][chance] = arr[y][x][chance] + 100
#                         q.append([ny, nx, d, chance])
#                     else:
#                         if not chance:
#                             if not arr[ny][nx][1] or arr[ny][nx][1] >= arr[y][x][chance] + 100:
#                                 arr[ny][nx][1] = arr[y][x][chance] + 100
#                                 q.append([ny, nx, d, 1])
#                 else:
#                     if not arr[ny][nx][chance] or arr[ny][nx][chance] >= arr[y][x][chance] + 600:
#                         arr[ny][nx][chance] = arr[y][x][chance] + 600
#                         q.append([ny, nx, d, chance])
#                     else:
#                         if not chance:
#                             if not arr[ny][nx][1] or arr[ny][nx][1] >= arr[y][x][chance] + 600:
#                                 arr[ny][nx][1] = arr[y][x][chance] + 600
#                                 q.append([ny, nx, d, 1])
#     print(answer-100)
#
solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]])