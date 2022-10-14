# n이 최대 200으로 floyd warshall이 가능해보임
# 다익스트라 시간 초과 발생

def solution(n, s, a, b, fares):
    adj = [[1e10] * (n + 1) for _ in range(n + 1)]
    
    for v in range(1, n + 1):
        adj[v][v] = 0
    
    for v1, v2, w in fares:
        adj[v1][v2] = w
        adj[v2][v1] = w
    
    
    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                adj[start][end] = min(adj[start][mid] + adj[mid][end], adj[start][end])

    answer = adj[s][a] + adj[s][b]
    for mid in range(1, n + 1):
        if mid == s: continue
        answer = min(answer, adj[s][mid] + adj[mid][a] + adj[mid][b], adj[s][mid] + adj[mid][a] + adj[a][b], adj[s][mid] + adj[mid][b] + adj[b][a])
    
    return answer


# 시간 초과 났던 다익스트라
# from heapq import heappop, heappush


# def dijkstra(adj, start, end):
#     Q = [(start, 0)]
#     visit = set()
    
#     while Q:
#         curV, curCost = heappop(Q)
#         if curV in visit: continue
#         if curV == end: return curCost
#         visit.add(curV)
    
#         for neiV, neiCost in adj[curV]:
#             if neiV not in visit:
#                 heappush(Q, (neiV, curCost + neiCost))
    
#     return 10 ** 10


# def solution(n, s, a, b, fares):
#     adj = [[] for _ in range(n + 1)]
#     for v1, v2, w in fares:
#         adj[v1].append((v2, w))
#         adj[v2].append((v1, w))

#     startToA = dijkstra(adj, s, a)
#     startToB = dijkstra(adj, s, b)
#     # aToB = dijkstra(adj, a, b)
    
#     minV = startToA + startToB  # 처음부터 따로 가는 경우
    
#     # 시간초과 날듯
#     for mid in range(1, n + 1):
#         startToMid = dijkstra(adj, s, mid)
#         midToA = dijkstra(adj, mid, a)
#         midToB = dijkstra(adj, mid, b)
#         minV = min(minV, startToMid + midToA + midToB)
    
#     answer = minV
#     return answer
