def solution(rows, columns, queries):
    answer = []
    G = []
    for row in range(rows):
        G.append([i for i in range(row * columns + 1, (row + 1) * columns + 1)])
    for querie in queries:
        querie = [i - 1 for i in querie]
        tmp = G[querie[0]][querie[1]]
        minV = tmp

        for i in range(querie[0] + 1, querie[2] + 1):
            G[i - 1][querie[1]] = G[i][querie[1]]
            minV = min(minV, G[i][querie[1]])

        for i in range(querie[1] + 1, querie[3] + 1):
            G[querie[2]][i - 1] = G[querie[2]][i]
            minV = min(minV, G[querie[2]][i])

        for i in range(querie[2] - 1, querie[0] - 1, -1):
            G[i + 1][querie[3]] = G[i][querie[3]]
            minV = min(minV, G[i][querie[3]])

        for i in range(querie[3] - 1, querie[1] - 1, -1):
            G[querie[0]][i + 1] = G[querie[0]][i]
            minV = min(minV, G[querie[0]][i])

        G[querie[0]][querie[1] + 1] = tmp

        answer.append(minV)

    return answer