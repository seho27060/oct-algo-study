from heapq import heappop, heappush
import math
INF = math.inf

def dijkstra(graph, start):
    lst = [INF for _ in range(len(start)+1)]
    lst[graph] = 0
    #start
    hq = [[graph, 0]]

    while hq:
        node, fee = heappop(hq)
        for node2, fee2 in start[node]:
            fee2 += fee
            if lst[node2] > fee2: #작으면 업데이트
                lst[node2] = fee2
                heappush(hq, [node2, fee2])
    return lst

def solution(n, s, a, b, fares):
    answer = 1000000000

    graph = [[] for _ in range(n+1)]

    for i in fares:
        graph[i[0]].append([i[1], i[2]])
        graph[i[1]].append([i[0], i[2]])

    for i in range(1, n+1):
        d = dijkstra(i, graph)
        result = d[s] + d[a] + d[b]
        if answer> result:
            answer = result

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))