#221024 행렬 테두리 회전하기
# n*m <=100*100
# 1 ~ n*m의 값이 행렬로 구성..
# 주어진 쿼리의 테두리를 돌려돌려

def solution(rows, columns, queries):
    answer = []

    board =[]
    cnt = 0
    for row in range(rows):
        addRow = []
        for col in range(columns):
            cnt += 1
            addRow.append(cnt)
        board.append(addRow)

    for [x1, y1, x2, y2] in queries:

        upLine = board[x1 - 1][y1-1:y2].copy()
        downLine = board[x2 - 1][y1-1:y2].copy()
        leftLine = []
        rightLine = []
        for x in range(x1-1,x2):
            leftLine.append(board[x][y1-1])
            rightLine.append(board[x][y2-1])
        result = 10e9
        # 상하 2 ~ n 복사 붙이기
        idx = 0
        for y in range(y1-1,y2):
            if y + 1 <= y2 - 1:
                board[x1-1][y + 1] = upLine[idx]
                board[x2-1][y] = downLine[idx+1]
                result = min([result,upLine[idx],downLine[idx+1]])
            idx += 1
        # 좌우
        idx = 0
        for x in range(x1-1,x2):
            if x + 1 <= x2 - 1:
                board[x][y1-1] = leftLine[idx+1]
                board[x+1][y2-1] = rightLine[idx]
                result = min([result,leftLine[idx+1],rightLine[idx]])
            idx += 1
        answer.append(result)

    return answer
