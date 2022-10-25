# 아주 정직한 브루트포스 문제
# 제발 행과 열을 혼동하게하는 x, y사용 너무 싫다...
# 국어 실력의 필요성을 느낀 문제

from collections import deque

def solution(rows, columns, queries):
    answer = []
    arr = [[] for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            arr[row].append(row*columns + (column+1))

    print(arr)
    def move(c1, r1, c2, r2):
        q = deque()
        for i in range(r1-1, r2):
            q.append(arr[c1-1][i])
        for i in range(c1, c2-1):
            q.append(arr[i][r2-1])
        for i in range(r2-1, r1-2, -1):
            q.append(arr[c2-1][i])
        for i in range(c2-2, c1-1, -1):
            q.append(arr[i][r1-1])
        val = q.pop()
        q.appendleft(val)

        answer.append(min(q))

        idx = 0
        for i in range(r1-1, r2):
            arr[c1-1][i] = q[idx]
            idx += 1
        for i in range(c1, c2-1):
            arr[i][r2-1] = q[idx]
            idx += 1
        for i in range(r2-1, r1-2, -1):
            arr[c2-1][i] = q[idx]
            idx += 1
        for i in range(c2-2, c1-1, -1):
            arr[i][r1-1] = q[idx]
            idx += 1

    for query in queries:
        c1, r1, c2, r2 = query
        move(c1, r1, c2, r2)

    # return answer
    print(answer)
solution(6, 7, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])