import heapq, sys

inf = sys.maxsize


def dijk(s, n, G):
    d = [inf] * (n + 1)
    q = []
    d[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in G[now]:
            cost = dist + i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost

                heapq.heappush(q, (cost, i[0]))
    return d


def solution(n, s, a, b, fares):
    answer = sys.maxsize
    G = [[] for _ in range(n + 1)]
    for i in fares:
        t, m, c = i[0], i[1], i[2]
        G[t].append((m, c))
        G[m].append((t, c))

    start = dijk(s, n, G)
    a_end = dijk(a, n, G)
    b_end = dijk(b, n, G)

    for i in range(1, n + 1):
        val = start[i] + a_end[i] + b_end[i]
        if answer > val:
            answer = val

    return answer