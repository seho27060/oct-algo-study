from collections import deque

def bfs(place):
    people = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append([i, j])

    for p in people:
        q = deque([p])
        visited = [[False] * 5 for _ in range(5)]
        visited[p[0]][p[1]] = True

        dist = [[0] * 5 for _ in range(5)]

        while q:
            x, y = q.popleft()

            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            for d in range(4):
                newx = x + dx[d]
                newy = y + dy[d]

                if 0 <= newx < 5 and 0 <= newy < 5 and visited[newx][newy] == False:
                    if place[newx][newy] == "P" and dist[x][y] < 2:
                        return 0

                    if place[newx][newy] == "O":
                        q.append([newx, newy])
                        visited[newx][newy] = True
                        dist[newx][newy] = dist[x][y] + 1

    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer