def solution(rows, columns, queries):
    def dolldoll(y1, x1, y2, x2):
        n = rows*columns+1

        A = ARR[y1-1 ][x2 - 1]
        for i in reversed(range(x1, x2)):
            ARR[y1 - 1][i] = ARR[y1 - 1][i - 1]
            if ARR[y1 - 1][i] < n:
                n = ARR[y1 - 1][i]

        for i in range(y1-1, y2-1):
            ARR[i][x1-1] = ARR[i + 1][x1 - 1]
            if ARR[i][x1 - 1] < n:
                n = ARR[i][x1 - 1]

        for i in range(x1-1, x2-1):
            ARR[y2 - 1][i] = ARR[y2-1][i+1]
            if ARR[y2 - 1][i] < n:
                n = ARR[y2 - 1][i]

        for i in reversed(range(y1, y2)):
            ARR[i][x2 - 1] = ARR[i - 1][x2 - 1]
            if ARR[i][x2 - 1] < n:
                n = ARR[i][x2 - 1]

        ARR[y1][x2 - 1] = A
        if ARR[y1][x2 - 1] < n:
            n = ARR[y1][x2 - 1]

        answer.append(n)

    ARR = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            ARR[i][j] = cnt
            cnt += 1

    answer = []
    for t in range(len(queries)):
        dolldoll(queries[t][0],queries[t][1],queries[t][2],queries[t][3])

    print(answer)
    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])