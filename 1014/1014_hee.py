import sys
from heapq import *
INF = sys.maxsize

def dijk(s, arr, G):
    arr[s] = 0
    Q = [(0, s)]
    while Q:
        c, n1 = heappop(Q)
        
        if arr[n1] < c:
            continue
        
        for cost, n2 in G[n1]:
            if arr[n1] + cost < arr[n2]:
                arr[n2] = arr[n1] + cost
                heappush(Q,(arr[n2], n2))

    return arr

def solution(n, s, a, b, fares):
    G = [[] for _ in range(n+1)] 
    for x, y, z in fares:
        G[x].append((z, y))
        G[y].append((z, x))
    
    arr_size = n * (n-1) // 2
    D_S = dijk(s, [INF] * arr_size, G)
    D_A = dijk(a, [INF] * arr_size, G)
    D_B = dijk(b, [INF] * arr_size, G)
    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, D_S[i] + D_A[i] + D_B[i])
        
    return answer