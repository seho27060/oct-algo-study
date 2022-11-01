# 효율성은 카페가서 다시 도전하겠읍니다...
# 힙큐로 정렬하고 순회하려했는데 얘 왜 실행하면 다 실패뜸...??
import heapq
from collections import deque

def solution(info, query):
    answer = []
    datas = []
    q = deque()
    for _ in info:
        lng, po, ex, fa, sc = _.split()
        datas.append((int(sc) * (-1), lng, po, ex, fa))
    heapq.heapify(datas)

    for i in query:
        lng, a1, po, a2, ex, a3, fa, sc = i.split()
        q.append((int(sc), lng, po, ex, fa))

    while q:
        cnt = 0
        req = q.popleft()
        for data in datas:
            if req[0] <= abs(data[0]):
                if req[1] != '-' and req[1] != data[1]:
                    continue
                if req[2] != '-' and req[2] != data[2]:
                    continue
                if req[3] != '-' and req[3] != data[3]:
                    continue
                if req[4] != '-' and req[4] != data[4]:
                    continue
                cnt += 1
            else:
                break
        answer.append(cnt)
    print(answer)

solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])