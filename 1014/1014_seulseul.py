import heapq
import sys

def solution(n, s, a, b, fares):
    maps = [[] for _ in range(n+1)]
    for x, y, z in fares:
        maps[x].append([z, y])
        maps[y].append([z, x])
    INF = sys.maxsize
    
    def dijkstra(start):
        distance = [INF] * (n+1)
        # 시작점까지 값 = 0
        distance[start] = 0
        heap = []
        heapq.heappush(heap, [0, start])
        while heap:
            # 현재까지 거리, 현 위치
            dist, now = heapq.heappop(heap)
            # 효율성 유지용. 이미 더 짧은 거리가 있다면 계산할필요 X 
            if distance[now] < dist:
                continue
            for cost, next in maps[now]:
                new_distance = dist+cost
                if distance[next] > new_distance:
                    distance[next] = new_distance
                    heapq.heappush(heap, [new_distance, next])
        return distance
    
    x = [[]] + [dijkstra(i) for i in range(1, n+1)]
    ans = INF
    for i in range(1, n+1):
        ans = min(x[i][a]+x[i][b]+x[i][s], ans)
    return ans