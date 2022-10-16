import heapq


def solution(n, s, a, b, fares):
    def djk(s):
        A = [100001 * n] * (n + 1)
        A[s] = 0

        L = [(0, s)]
        while L:
            cnt, now = heapq.heappop(L)

            if A[now] > cnt:
                continue

            for c, next in road[now]:
                if A[next] > c + cnt:
                    A[next] = c + cnt
                    heapq.heappush(L, [c + cnt, next])

        return A

    road = {i: [] for i in range(1, n + 1)}
    for c, d, g in fares:
        road[c].append([g, d])
        road[d].append([g, c])

    answer = 100001 * n

    together = djk(s)
    for i in range(1, n + 1):
        if together[i] != 100001:
            go = djk(i)
            answer = min(answer, together[i] + go[a] + go[b])

    return answer