import heapq
import collections

def solution(n, s, a, b, fares):
    global graph
    answer = 0
    graph = collections.defaultdict(list)
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dijkstra(x, y):
        global graph
        dist = [1e9] * (n + 1)
        q = [(0, x)]
        dist[x] = 0
        while q:
            x, node = heapq.heappop(q)
            if dist[node] < x:
                continue
            for v, w in graph[node]:
                if x + w < dist[v]:
                    dist[v] = x + w
                    heapq.heappush(q, (x + w, v))
        return dist[y]

    cost = dijkstra(s, a) + dijkstra(s, b)
    for i in range(1, n + 1):
        cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    answer = cost

    return answer