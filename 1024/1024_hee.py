def rotation(x1, y1, x2, y2, G):
    c, r = x2 - x1, y2 - y1
    temp = G[x1][y1]
    ans = temp

    for i in range(c):
        G[x1 + i][y1] = G[x1 + i + 1][y1]
        ans = min(ans, G[x1 + i][y1])

    for i in range(r):
        G[x2][y1 + i] = G[x2][y1 + i + 1]
        ans = min(ans, G[x2][y1 + i])

    for i in range(c, 0, -1):
        G[x1 + i][y2] = G[x1 + i - 1][y2]
        ans = min(ans, G[x1 + i][y2])

    for i in range(r, 0, -1):
        G[x1][y1 + i] = G[x1][y1 + i - 1]
        ans = min(ans, G[x1][y1 + i])

    G[x1][y1 + 1] = temp
    return G, ans


def solution(rows, columns, queries):
    answer = []
    G = [[columns * j + i for i in range(1, columns + 1)] for j in range(rows)]
    for x1, y1, x2, y2 in queries:
        G, ans = rotation(x1 - 1, y1 - 1, x2 - 1, y2 - 1, G)
        answer.append(ans)
    return answer
