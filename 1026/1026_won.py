from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def f(place):
    arr = []
    for i in range(5):
        for k in range(5):
            if place[i][k] == 'P':
                arr.append([i, k])

    for sr, sc in arr:
        qu = deque()
        qu.append([sr, sc])
        visited = [[0] * 5 for _ in range(5)]
        visited[sr][sc] = 1
        while qu:
            cr, cc = qu.popleft()

            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] == 0:
                    if place[nr][nc] == 'O':
                        visited[nr][nc] = visited[cr][cc] + 1
                        qu.append([nr, nc])
                    if place[nr][nc] == 'P' and visited[cr][cc] <= 2:
                        return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        res = f(place)
        answer.append(res)
    return answer