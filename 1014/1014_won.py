from heapq import heappush, heappop


def d(n, s, e, G):
    INF = float('inf')
    dist = [INF] * (n + 1)
    qu = []
    qu.append([0, s])
    dist[s] = 0
    while qu:
        cur_dist, cur_node = heappop(qu)

        if dist[cur_node] > cur_dist:
            continue

        for new_dist, new_node in G[cur_node]:
            if dist[new_node] > cur_dist + new_dist:
                dist[new_node] = cur_dist + new_dist
                heappush(qu, [cur_dist + new_dist, new_node])
    return dist[e]

def solution(n, s, a, b, fares):
    answer = 0
    G = [[] for _ in range(n + 1)]
    for fare in fares:
        u, v, w = map(int, fare)
        G[u].append([w, v])
        G[v].append([w, u])
    # 따로 갔을 때가 초기값
    answer = d(n, s, a, G) + d(n, s, b, G)
    for i in range(1, n + 1):
        if i == s:
            continue
        answer = min(answer, d(n, s, i, G) + d(n, i, a, G) + d(n, i, b, G))
    return answer