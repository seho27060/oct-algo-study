def rotate(x1, y1, x2, y2, newX, newY):
    D = {
        'upwards': (-1, 0), 
        'downwards': (1, 0), 
        'toRight': (0, 1), 
        'toLeft': (0, -1)
    }

    top = x1 - 1
    bottom = x2 - 1
    left = y1 - 1
    right = y2 - 1

    if newX == top and newY != right:
        return D['toRight']
    if newX != bottom and newY == right:
        return D['downwards']
    if newX == bottom and newY != left:
        return D['toLeft']
    if newX != top and newY == left:
        return D['upwards']


def findEdge(board, x1, y1, x2, y2):
    # list, int, int, int -> int, list
    edges = []
    minV = 100_000
    for row in range(x1 - 1, x2):
        for col in range(y1 - 1, y2):
            if row in (x1 - 1, x2 - 1) or col in (y1 - 1, y2 - 1):
                edges.append((board[row][col], row, col, rotate(x1, y1, x2, y2, row, col)))
                minV = min(minV, board[row][col])
    return minV, edges


def applyRotation(board, edges):
    for val, row, col, (dx, dy) in edges:
        board[row + dx][col + dy] = val


def solution(rows, columns, queries):
    board = [[0] * columns for _ in range(rows)]

    num = 1
    for row in range(rows):
        for col in range(columns):
            board[row][col] = num
            num += 1

    answer = []
    for x1, y1, x2, y2 in queries:
        minV, edges = findEdge(board, x1, y1, x2, y2)
        answer.append(minV)
        applyRotation(board, edges)

    return answer
