# 원래는 다익 2번을 활용해서 문제 풀이 진행
# 일단 시작점 기준으로 다른 노드로 향하는 최소 거리를 탐색
# 다른 노드로 이동할 때 기 노드 기준으로 a, b로 가는 각각의 최소거리 합이 구해져있지 않다면 구해서 리스트에 저장해두기

from collections import deque

def solution(n, s, a, b, fares):
    G = [[] for _ in range(n + 1)]
    for fare in fares:
        now, next, dis = fare
        G[now].append([next, dis])
        G[next].append([now, dis])

    def dijk1(node, ans):
        with_D = [1000000000] * (n + 1)
        sep_D = [0] * (n + 1)
        with_D[node] = 0
        q = deque()
        q.append([node, 0])
        while q:
            now, dis = q.popleft()
            if dis > with_D[now]:
                continue
            if not sep_D[now]:
                sep_D[now] = dijk2(now)
            if dis + sep_D[now] < ans:
                ans = dis + sep_D[now]
            for next, d in G[now]:
                if dis + d < with_D[next]:
                    with_D[next] = dis + d
                    q.append([next, with_D[next]])
        return ans

    def dijk2(node):
        D = [1000000000] * (n + 1)
        D[node] = 0
        q = deque()
        q.append([node, 0])
        while q:
            now, dis = q.popleft()
            if dis > D[now]:
                continue
            for next, d in G[now]:
                if dis + d < D[next]:
                    D[next] = dis + d
                    q.append([next, D[next]])
        return D[a] + D[b]

    return dijk1(s, 1000000000)