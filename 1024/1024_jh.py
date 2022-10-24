def solution(rows, columns, queries):
    answer = []
    array = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    value = 1

    for i in range(1, rows+1):
        for j in range(1, columns+1):
            array[i][j] = value
            value += 1

    for q in queries:
        #x1 0, y1 1, x2 2, y2 3
        tmp = array[q[0]][q[1]]
        minV = tmp

        # 위에서 아래
        for i in range(q[0], q[2]):
            tmp2 = array[i+1][q[1]]
            array[i][q[1]] = tmp2
            minV = min(minV, tmp2)

        #왼 -> 오
        for i in range(q[1], q[3]):
            tmp2 = array[q[2]][i+1]
            array[q[2]][i] = tmp2
            minV = min(minV, tmp2)

        # 아래 -> 위
        for i in range(q[2], q[0], -1):
            tmp2 = array[i-1][q[3]]
            array[i][q[3]] = tmp2
            minV = min(minV, tmp2)

        #오 -> 왼
        for i in range(q[3], q[1], -1):
            tmp2 = array[q[0]][i - 1]
            array[q[0]][i] = tmp2
            minV = min(minV, tmp2)

        array[q[0]][q[1]+1] = tmp
        answer.append(minV)

    return answer