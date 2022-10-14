#221014 합승 택시 요금
from heapq import *

n, s, a, b, fares = 6,4,6,2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
n, s, a, b, fares = 7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

def solution(n, s, a, b, fares):
    answer = 10e9
    graphs = [[] for _ in range(n+1)]

    for fare in fares:
        graphs[fare[0]].append([fare[1],fare[2]])
        graphs[fare[1]].append([fare[0],fare[2]])
    # 각 위치에서 나머지 위치까지 최단거리 구하기
    startToEnd = [[0]*(n+1)]
    # print(graphs)
    for start in range(1,n+1):
        result = [10e9 for _ in range(n+1)]
        result[start] = 0
        queue = []
        heappush(queue,[0,start])

        while queue:
            cost, now = heappop(queue)
            for [nxt,nxtCost] in graphs[now]:
                if result[nxt] > cost + nxtCost:
                    result[nxt] = cost+nxtCost
                    heappush(queue,[cost+nxtCost,nxt])
        startToEnd.append(result)
    #
    # for kk in startToEnd:
    #     print(kk)

    for mid in range(1,n+1):
        answer = min(answer,startToEnd[mid][s]+startToEnd[mid][a]+startToEnd[mid][b])

    return answer

print(solution(n,s,a,b,fares))