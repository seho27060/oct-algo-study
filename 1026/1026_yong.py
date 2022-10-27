# 아마 단순 구현문제...?
# P기준으로 상하좌우 탐색해서 1차 탐색 > P가 있으면 False, O가 있으면 큐에 추가
# 추가된 Q를 기준으로 상하좌우 2차 탐색 > P가 있으면 False, 없으면 True

from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def solution(places):
    answer = []
    def find(i, j):
        q = deque()
        visited = []
        visited.append((i, j))
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if place[ny][nx] == 'O':
                    q.append([ny, nx])
                    visited.append((ny, nx))
                elif place[ny][nx] == 'P':
                    return False
        while q:
            y, x = q.popleft()
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < 5 and 0 <= nx < 5 and (ny, nx) not in visited:
                    if place[ny][nx] == 'O':
                        visited.append((ny, nx))
                    elif place[ny][nx] == 'P':
                        return False
        return True

    def check():
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not find(i, j):
                        return False
        return True

    for place in places:
        if check():
            answer.append(1)
        else:
            answer.append(0)
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])