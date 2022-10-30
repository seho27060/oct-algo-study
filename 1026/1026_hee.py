from collections import deque

def solution(places):
    answer = []
    for place in places:
        N = 5
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = 1
        for i in range(N):
            for j in range(N):
                if place[j][i] == 'P':
                    V = [[False] * N for _ in range(N)]
                    V[j][i] = True
                    Q = deque([(0, i, j)])
                    while Q:
                        c, x, y = Q.popleft()
                        for dx, dy in D:
                            nx = x + dx
                            ny = y + dy
                            if -1 < nx < N and -1 < ny < N and not V[ny][nx]:
                                if place[ny][nx] == 'P':
                                    ans = 0
                                elif place[ny][nx] == 'O':
                                    if c == 0:
                                        Q.append((1, nx, ny))
                                V[ny][nx] = True
        answer.append(ans)
    return answer