from collections import deque


def solution(rows, columns, queries):
    arr = [[(columns * j) + (i + 1) for i in range(columns)] for j in range(rows)]

    answer = []

    for x1, y1, x2, y2 in queries:
        q = deque()

        for i in range(y1, y2):
            q.append(arr[x1 - 1][i - 1])
        for i in range(x1, x2):
            q.append(arr[i - 1][y2 - 1])
        for i in range(y2, y1, -1):
            q.append(arr[x2 - 1][i - 1])
        for i in range(x2, x1, -1):
            q.append(arr[i - 1][y1 - 1])

        q.rotate(1)
        answer.append(min(q))

        for i in range(y1, y2):
            arr[x1 - 1][i - 1] = q.popleft()
        for i in range(x1, x2):
            arr[i - 1][y2 - 1] = q.popleft()
        for i in range(y2, y1, -1):
            arr[x2 - 1][i - 1] = q.popleft()
        for i in range(x2, x1, -1):
            arr[i - 1][y1 - 1] = q.popleft()

    return answer